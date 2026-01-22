#!/usr/bin/env bash
set -euo pipefail

# Vérifier que les templates existent
if [ ! -f ".openapi-generator/templates/api.mustache" ]; then
    echo "Warning: Custom template api.mustache not found"
    echo "The generator will use default templates"
fi

# ./scripts/add-custom-field-extensions.sh


# Remove generated files
for F in $(cat .openapi-generator/FILES) ; do
    rm -f "${F}"
done

# Generate library
docker run --rm --env JAVA_OPTS=-DmaxYamlCodePoints=9999999 -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.11.0 \
    generate \
    --config /local/.openapi-generator/config.yaml \
    --input-spec /local/api/openapi.yaml \
    --output /local \
    --inline-schema-options RESOLVE_INLINE_ENUMS=true \
    --http-user-agent go-netbox/$(cat api/netbox_version)


# rm -f api/openapi.yaml