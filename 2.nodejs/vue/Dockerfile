# base image
FROM node:14-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY /frontend/package.json /app/package.json
RUN yarn install
COPY /frontend /app/
# start app
CMD ["yarn", "serve"]