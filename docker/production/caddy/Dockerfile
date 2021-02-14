
# We utilize the multi stage build pattern to create a temporary image called
# build to compile the static React files, these are then copied over to the
# Caddy production image.

# Build image, based on node.
FROM node:14.4.0 as build
ARG build_script
WORKDIR /app
COPY ./react/package.json ./package.json
COPY ./react/package-lock.json ./package-lock.json
COPY ./react/src ./src
RUN npm install
COPY ./react/jsconfig.json ./jsconfig.json
COPY ./react/public ./public
RUN npm run ${build_script}

# Production image, Caddy, used to serve both the static react files, any
# static files from django, and as a regular reverse proxy.

FROM abiosoft/caddy:0.11.0
COPY ./docker/production/caddy/Caddyfile /etc/Caddyfile

COPY --from=build /app/build /srv/react


