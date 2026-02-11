#!/usr/bin/env python3
import yaml
import re
import shutil
from datetime import datetime
SPEC_PATH = 'api/openapi.yaml'
def backup_openapi_file(spec_path):
    """
    Creates a backup copy of the OpenAPI file with a timestamp.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{spec_path}.backup_{timestamp}"
    shutil.copy2(spec_path, backup_path)
    print(f"💾 Backup created: {backup_path}\n")
    return backup_path
# ==============================================================================
# Models filter
# ==============================================================================
MODELS_TO_FILTER = [
    'VPC',
    'Subnet',
    'SubnetPurpose',
    'SubnetPrefix',
    'SubnetIPAddress',
    'Environment',
    'Region',
    'Tenant',
    'TenantGroup',
    'CustomField',
    'Site',
    'SiteGroup',
    'Group',
    'ObjectPermission',
]
# ==============================================================================
def find_refs_in_object(obj, found_refs):
    """
    Recursive function to find all '$ref' references in an object.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == '$ref' and isinstance(value, str):
                match = re.search(r'#/components/schemas/(\w+)', value)
                if match:
                    found_refs.add(match.group(1))
            else:
                find_refs_in_object(value, found_refs)
    elif isinstance(obj, list):
        for item in obj:
            find_refs_in_object(item, found_refs)
def resolve_all_dependencies(initial_models, all_schemas):
    """
    Recursively resolves ALL transitive dependencies.
    """
    final_models = set()
    models_to_process = set(initial_models)
    while models_to_process:
        model_name = models_to_process.pop()
        
        if model_name in final_models:
            continue
            
        if model_name not in all_schemas:
            print(f"  ⚠️  Model '{model_name}' referenced but not found in schemas")
            continue
        final_models.add(model_name)
        
        schema = all_schemas[model_name]
        dependencies = set()
        find_refs_in_object(schema, dependencies)
        
        models_to_process.update(dependencies)
    return final_models

def path_matches_model(path_str, model_name):
    """
    Check if a path matches a model name, handling kebab-case URLs.
    Examples:
      - CustomField matches /custom-fields/
      - SubnetPrefix matches /subnet-prefixes/
    """
    # Convert CamelCase to kebab-case
    kebab = re.sub(r'(?<!^)(?=[A-Z])', '-', model_name).lower()
    
    # Try both singular and plural forms
    patterns = [
        r'/{}(s)?(/|$)'.format(re.escape(model_name.lower())),  # customfield(s)
        r'/{}(s)?(/|$)'.format(re.escape(kebab)),                # custom-field(s)
    ]
    
    return any(re.search(pattern, path_str.lower()) for pattern in patterns)

# Load the spec file
with open(SPEC_PATH, 'r') as file:
    data = yaml.load(file, Loader=yaml.CLoader)
if MODELS_TO_FILTER:
    print(f"Filtering specification for: {MODELS_TO_FILTER}\n")
    
    all_schemas = data.get('components', {}).get('schemas', {})
    original_paths = data.get('paths', {}).copy()
    
    # STEP 1: Identify relevant paths WITHOUT filtering schemas
    print("📍 Step 1: Identifying relevant endpoints...")
    relevant_paths_info = {}
    models_from_paths = set()
    
    for path_str, path_item in original_paths.items():
        path_is_relevant = False
        relevant_methods = {}
        
        # Check 1: Does the URL contain one of our models?
        for model_name in MODELS_TO_FILTER:
            if path_matches_model(path_str, model_name):
                path_is_relevant = True
                # Collect ALL methods for this path
                for method, operation in path_item.items():
                    if isinstance(operation, dict):
                        if method not in relevant_methods:  # Avoid duplicates
                            relevant_methods[method] = operation
                        refs = set()
                        find_refs_in_object(operation, refs)
                        models_from_paths.update(refs)
                # DON'T break - continue checking other models
        
        # Check 2: Does an operation directly reference our models?
        for method, operation in path_item.items():
            if not isinstance(operation, dict):
                continue
                
            refs = set()
            find_refs_in_object(operation, refs)
            
            if not refs.isdisjoint(set(MODELS_TO_FILTER)):
                path_is_relevant = True
                if method not in relevant_methods:  # Avoid duplicates
                    relevant_methods[method] = operation
                models_from_paths.update(refs)
        
        if path_is_relevant:
            relevant_paths_info[path_str] = relevant_methods
    
    print(f"  ✓ {len(relevant_paths_info)} relevant endpoints identified")
    print(f"  ✓ {len(models_from_paths)} models referenced in these endpoints\n")
    
    # STEP 2: Resolve ALL dependencies
    print("📍 Step 2: Resolving transitive dependencies...")
    all_required_models = set(MODELS_TO_FILTER) | models_from_paths
    final_models_to_keep = resolve_all_dependencies(all_required_models, all_schemas)
    
    # Statistics
    print(f"\n📊 Statistics:")
    print(f"  - Requested models: {len(MODELS_TO_FILTER)}")
    print(f"    {sorted(MODELS_TO_FILTER)}")
    
    models_from_endpoints = models_from_paths - set(MODELS_TO_FILTER)
    if models_from_endpoints:
        print(f"\n  - Models from endpoints: {len(models_from_endpoints)}")
        for model in sorted(models_from_endpoints):
            print(f"    + {model}")
    
    transitive = final_models_to_keep - all_required_models
    if transitive:
        print(f"\n  - Transitive dependencies: {len(transitive)}")
        for model in sorted(transitive):
            print(f"    + {model}")
    
    print(f"\n  - TOTAL: {len(final_models_to_keep)} models kept\n")
    
    # STEP 3: Filter schemas
    print("📍 Step 3: Filtering schemas...")
    data['components']['schemas'] = {
        name: schema for name, schema in all_schemas.items() 
        if name in final_models_to_keep
    }
    print(f"  ✓ {len(data['components']['schemas'])} schemas kept\n")
    # STEP 4: Filter paths
    print("📍 Step 4: Filtering endpoints...")
    data['paths'] = {}
    for path_str, relevant_methods in relevant_paths_info.items():
        data['paths'][path_str] = relevant_methods
    print(f"  ✓ {len(data['paths'])} endpoints kept\n")
    # STEP 5: Final verification
    print("🔍 Consistency check...")
    broken = []
    
    for path_str, path_item in data['paths'].items():
        for method, operation in path_item.items():
            if not isinstance(operation, dict):
                continue
            refs = set()
            find_refs_in_object(operation, refs)
            
            missing = refs - final_models_to_keep
            
            if missing:
                broken.append({
                    'endpoint': f"{method.upper()} {path_str}",
                    'missing': sorted(list(missing))
                })
    
    if broken:
        print("❌ Missing dependencies detected:")
        for op in broken:
            print(f"  {op['endpoint']}")
            print(f"    Missing: {', '.join(op['missing'])}")
    else:
        print("✅ No missing dependencies!\n")
        
# backup_openapi_file(SPEC_PATH)
if 'components' in data and 'schemas' in data['components']:
    for name, schema in data['components']['schemas'].items():
        if 'properties' in schema:
            dynamic_non_required_props = []
            for propName, prop in schema['properties'].items():
                if 'enum' in prop and None in prop['enum']:
                    prop['enum'].remove(None)
                if 'properties' in prop and 'value' in prop['properties'] and 'enum' in prop['properties']['value'] and None in prop['properties']['value']['enum']:
                    prop['properties']['value']['enum'].remove(None)
                if prop.get('nullable', False):
                    dynamic_non_required_props.append(propName)
            
            nullable_types = ['parent_device', 'primary_ip']
            for ntype in nullable_types:
                if ntype in schema['properties']:
                    schema['properties'][ntype]['nullable'] = True
                    if ntype not in dynamic_non_required_props:
                        dynamic_non_required_props.append(ntype)
            
            non_nullable_types = ['front_image', 'rear_image']
            for ntype in non_nullable_types:
                if ntype in schema['properties']:
                    if schema['properties'][ntype].get('format') == 'binary':
                        schema['properties'][ntype].pop('nullable', None)
        
            non_required_props = [
                'devicetype_count', 'device_count', 'virtualmachine_count',
                'prefix_count', 'vlan_count', 'display_url', 'user_count',
                'aggregate_count', 'asn_count', 'choices_count', 'circuit_count',
                'cluster_count', 'contact_count', 'file_count', 'interface_count',
                'inventoryitem_count', 'ipaddress_count', 'member_count',
                'platform_count', 'powerfeed_count', 'provider_count',
                'rack_count', 'site_count', 'tenant_count', 'terminations_count',
                'tunnel_count', 'vrf_count', 'wirelesslan_count', 'created',
                'provider_count', 'cable_end', 'allocated_vcpus',
                'allocated_memory', 'allocated_disk', 'tagged_items',
            ] + dynamic_non_required_props
            
            if 'required' in schema:
                schema['required'] = [prop for prop in schema['required'] 
                                     if prop not in non_required_props]
if 'Device' in data.get('components', {}).get('schemas', {}):
    if 'required' not in data['components']['schemas']['Device']:
        data['components']['schemas']['Device']['required'] = []
    device_props = data['components']['schemas']['Device'].get('properties', {})
    required_fields = ['id', 'url', 'display', 'name', 'description']
    for field in required_fields:
        if field in device_props and field not in data['components']['schemas']['Device']['required']:
             data['components']['schemas']['Device']['required'].append(field)
# Save
with open(SPEC_PATH, 'w') as file:
    yaml.dump(data, file, Dumper=yaml.CDumper, sort_keys=False)
print(f"✅ File {SPEC_PATH} modified successfully!")