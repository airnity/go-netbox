#!/bin/bash
# scripts/add-custom-field-extensions.sh

SPEC_FILE="api/openapi.yaml"
TEMP_SPEC="api/openapi-with-cf.yaml"

echo "Adding custom field extensions to OpenAPI spec..."

# Liste des endpoints qui supportent les custom fields
SUPPORTED_ENDPOINTS=(
    "ipam_ip_addresses_list"
    "ipam_prefix_list" 
)

# Copier le spec original
cp "$SPEC_FILE" "$TEMP_SPEC"

# Ajouter l'extension pour chaque endpoint supporté
for endpoint in "${SUPPORTED_ENDPOINTS[@]}"; do
    # Utiliser yq ou sed pour ajouter l'extension
    yq eval "(.paths.[] | select(.get.operationId == \"$endpoint\").get.\"x-supports-custom-fields\") = true" -i "$TEMP_SPEC"
done

echo "Custom field extensions added to $TEMP_SPEC"