# Using Alpine base image
FROM alpine:3.10


RUN groupadd -r lirantal && useradd -r -s /bin/false -g lirantal lirantal

WORKDIR /code
COPY ./code /code


USER 

RUN apk add --no-cache ca-certificates