FROM node:14.4.0

WORKDIR /app

# Install app dependencies here to make sure they're cached
COPY ./react/package.json ./package.json
COPY ./react/package-lock.json ./package-lock.json
RUN npm install

COPY ./docker/local/react/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./react/jsconfig.json ./jsconfig.json
COPY ./react/public ./public
