<h1 align="center">
  Recipe API
  <br>
</h1>

<h4 align="center">A minimal Recipe app that created with Django Rest Framework.</h4>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Language-Python-yellow"
         alt="Python">
  </a>
  <a href="https://djangoproject.com">
      <img src="https://img.shields.io/badge/Framework-Django-success"
           alt="Django">
  </a>
  <a href="https://www.django-rest-framework.org/">
    <img src="https://img.shields.io/badge/Lib-DRF-red" alt="DRF">
  </a>
  <a href="https://www.postgresql.org">
    <img src="https://img.shields.io/badge/Database-Postgersql-informational"
         alt="Postgresql">
  </a>
  <a href="https://www.docker.com">
    <img src="https://img.shields.io/badge/Virtualization-Docker-blue"
         alt="Postgresql">
  </a>
</p>

<p align="center">
  <a href="#Introduction">Introduction</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a>
</p>


## Introduction

DRF Recipe API, provides API endpoints for creating and managing user, recipes, tags and ingredients.


## Key Features

* Setting up project using Docker configuration.
* Use Github actions to run automate tests and linting.
* Adding endpoints for creating and managing user, recipes, tags and ingredients.
* Adding filtering to our list endpoints.
* Uploading images.
* Writing unit tests with TDD aproche.


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone git@github.com:amirzre/recipe-app-api.git

# Install Docker on your system, for debian and ubuntu
$ sudo apt install docker

# Install Docker Compose, for debian and ubuntu
$ sudo apt install docker-compose

# Go to the project directory
$ cd recipe-app-api

# build Docker images
$ sudo docker-compose build

# Do make migrations
$ sudo docker-compose run --rm app sh -c "python manage.py makemigrations"

# Run the project
$ sudo docker-compose run
```

> **Note**
> If you're using Windows, it's better to switch to `Linux` for easier access to tools.
