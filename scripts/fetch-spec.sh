#!/usr/bin/env bash

set -euo pipefail

# NETBOX_VERSION="$1"
# NETBOX_DOCKER_VERSION="$2"

REPO_DIR='/tmp/netbox-docker'

rm -rf "${REPO_DIR}"

# git clone https://github.com/netbox-community/netbox-docker.git \
#   --config advice.detachedHead=false \
#   --branch ${NETBOX_DOCKER_VERSION} \
#   --depth=1 \
#   --quiet \
#   "${REPO_DIR}"

# mv "${REPO_DIR}/docker-compose.override.yml.example" "${REPO_DIR}/docker-compose.override.yml"

# export VERSION="v${NETBOX_VERSION}"
# docker compose --project-directory="${REPO_DIR}" up --detach --quiet-pull

while ! curl --silent https://netbox.central.sandbox.airnity.private/api/schema/ > api/openapi.yaml 2> /dev/null; do
# while ! curl --silent https://netbox.netbox-airnity-plugin.orb.local/api/schema/ > api/openapi.yaml 2> /dev/null; do
  sleep 1
done

# docker compose --project-directory="${REPO_DIR}" down --volumes

rm -rf "${REPO_DIR}"
