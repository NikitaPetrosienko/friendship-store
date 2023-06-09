# build stage
FROM node:lts-alpine

WORKDIR /var/www/html/friendship_store

ENV PATH /var/www/html/friendship_store/node_modules/.bin:$PATH

COPY package.json /var/www/html/friendship_store/package.json

RUN yarn

EXPOSE 3000

COPY . .

CMD ["yarn", "dev"]