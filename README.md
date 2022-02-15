# Project Setup:

This repo consist of easy to configure development environments to begin projects. Each directory can be used as a submodule.

### Docker Images:

- radbydesign/vue
- radbydesign/django_api
  <!-- - radbydesign/express_api -->
  <!-- - radbydesign/basic_app -->

To build images:

- `cd /desired/directory`
- `docker-compose up`

## Docker

### What is Docker

Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. Docker desktop is required to use this repo.

#### Visit the site below for more details on installing docker desktop on your local machine.

https://www.docker.com/products/docker-desktop

### Running Images

- cd into project
- `docker-compose up`

### Using Git submodules:

- cd into your project folder
- for example: `git submodule add https://github.com/radbydesign/service/django_api`
- The contents of 1.python/django will be in your folder
- if the folder is empty try updating using:
- `git submodule update --init --recursive`
