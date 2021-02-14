
# We utilize the multi stage build pattern to create a temporary image we
# use to compile Caddy from scratch (so we can install plugins).



# Build React-image:
FROM node:14.4.0 AS react-builder
WORKDIR /app
COPY ./react/package.json ./package.json
COPY ./react/package-lock.json ./package-lock.json
COPY ./react/src ./src
RUN npm install
COPY ./react/jsconfig.json ./jsconfig.json
COPY ./react/public ./public
RUN npm run build


# Build Caddy-image:
FROM caddy:2.1.1-builder AS caddy-builder
RUN xcaddy build --with github.com/sillygod/cdp-cache

FROM caddy:2.1.1
COPY --from=caddy-builder /usr/bin/caddy /usr/bin/caddy

COPY --from=build /app/build /srv/react

COPY ./docker/production/caddy/Caddyfile /etc/Caddyfile