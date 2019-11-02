# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /code

# add `/app/node_modules/.bin` to $PATH
ENV PATH /code/node_modules/.bin:$PATH

# install and cache app dependencies
COPY . /code
RUN npm install

# start app
CMD ["npm", "run", "serve"]