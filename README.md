![Docker Series Builds](https://github.com/Collabmaker/CM_main/workflows/Docker%20Series%20Builds/badge.svg)

# Collabmaker
Connecting collaborators and people with great ideas during a time of need.


## Contents

- [Installation](README.md#installation)
  
  - [Git](README.md#git)
    - [Ubuntu 20.04](README.md#git-ubuntu)
    - [MacOS Catalina](README.md#git-mac)
    
  - [Docker](README.md#docker-ubuntu)
    - [Ubuntu 20.04](README.md#docker-ubuntu)
    - [MacOS Catalina](README.md#docker-mac)
  
  - [Setup the folder structure](README.md#setup-the-folder-structure)
  
  
  - [Confirm Installation](README.md#confirm-installation)

- [Local Development](README.md#local-development)

- [Single-server production](README.md#single-server-production)

- [The Stack](README.md#the-stack)

  - [Django](README.md#django)

  - [Postgresql](README.md#postgresql)

  - [React](README.md#react)

  - [Celery](README.md#celery)

  - [Redis](README.md#redis)

  - [Caddy](README.md#caddy)

  - [Kubernetes](README.md#kubernetes)
  
  - [Github Actions CI](README.md#github-actions-ci)
    
- [Docker Commands](README.md#docker-commands)

- [Database commands](README.md#database-commands)

- [Django testing](README.md#django-testing)

- [API Usage](README.md#api-usage)

## Installation
To keep the same environment locally as in the production environment, all development is handled through docker containers.
The only things you need to install locally are Docker and Git. Below is instructions on how to install for Ubuntu or Mac.

-------------------------------
### Git <a name="git"></a>

#### Ubuntu 20.04 <a name="git-ubuntu"></a>
1. Go to your terminal
2. Run `$ sudo apt install git`
3. Type in your password and it should install.

#### MacOS Catalina <a name="git-mac"></a>
1. Go to your terminal
2. Install homebrew: `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
3. Install Git: `$ brew install git`

-------------------------------

### Docker <a name="docker"></a>


#### Ubuntu 20.04 <a name="docker-ubuntu"></a>
1. Install docker through following these commands: https://www.hostinger.com/tutorials/how-to-install-docker-on-ubuntu
2. Run `sudo apt install docker-compose`
3. Change permissions to be able to run without sudo: https://docs.docker.com/engine/install/linux-postinstall/

#### MacOS Catalina <a name="docker-mac"></a>
1. Install Docker: https://docs.docker.com/get-docker/
2. Make sure Docker is running on your machine. (You should see a whale with containers)

-------------------------------

### Setup the folder structure
1. Navigate to where you want to keep your project folders ex: `$ cd Documents`
2. Create the folder to keep the repository: `$ mkdir Collabmaker`
3. Enter the folder: `$ cd Collabmaker`
4. Clone the repository: `$ git clone https://github.com/Collabmaker/CM_main.git`
5. Enter the repository root folder: `$ cd CM_main`


-------------------------------

### Confirm Installation

1. In your terminal, make sure you are inside the root of the `CM_main` repository folder.
2. Run the local setup Dockerfiles: `$ docker-compose -f compose/local.yml up --build`

That's it! If you have successfully installed `Git` and `Docker` on your system then the entire project should now install and start up.

Now docker will install `Django`, `Postgresql`, `React`, `Redis` and `Celery` etc in their respective containers and then start them up.

-------------------------------

## Local Development

To start the local development environment run:

`$ docker-compose -f compose/local.yml up --build`

It should start right up, no configuration from your part is required. It can
take a while as all the dependencies are installed for the first time.

Go ahead and visit http://localhost:8000 for the `Django` webserver and http://localhost:3000 
for the `React` app. in your browser. The project features live reloading, any changes you make in
the code should be apparent as soon as you refresh.

To run a management command, in this case opening an interactive interpreter, run:

`$ docker-compose -f compose/local.yml run --rm django python manage.py shell`

To run the django and react test suites, respectively, run:

`$ docker-compose -f compose/local.yml run --rm django python manage.py test`
`$ docker-compose -f compose/local.yml run --rm django react npm test`

-------------------------------

## Single-server production

To run the project in production on a single server requires some configuration
on your part. Ensure that Docker and Docker Compose is installed on the server,
add the missing environment variables to compose/.envs/.production, and run:

`$ docker-compose -f compose/production.yml up --build --detach`

Make sure to keep the compose/.envs/.production files out of version control.
The missing environment variables are primarily authentication credentials.

To run a management command, in this case ´migrate´, run:

`$ docker-compose -f compose/production.yml run --rm django python manage.py migrate`

To check on the logs run::

`$ docker-compose -f compose/production.yml logs`

To see how your containers are doing, and performance metrics, respectively,
run:

`$ docker-compose -f compose/production.yml ps`
`$ docker stats`

If you need to scale the application, run:

`$ docker-compose -f compose/production.yml up --scale django=4`

Do not scale PostgreSQL, Caddy or Redis, as those are not configured to scale.
If the performance of either becomes a bottle-neck, deploy the application on
multi-server setup using Kubernetes.

-------------------------------

## The Stack

<div align="center">
	<img width="900" height="600" src="Documentation/images/Microservices_System_Design.png" alt="System Design">
	<br>
	<br>
	<br>
</div>

#### Get Django shell
`docker-compose -f compose/local.yml run django python manage.py shell`

#### Import populate_db to populate database
`from Python_scripts.Populate_db import populate`

#### Django
In the backend we use the `Django` webframework to handle everything from building Rest APIs to authentication and ORM to better integrate with the database.

#### Postgresql
For database we use `Postgresql` for it's open source nature and support for when we want to include geographical data with postgis.

#### React
For frontend we use `React`. The way we have structured the project is that in `React` we mainly consume the APIs built in `Django` and most of the computation is done on the backend `Django` server.

#### Celery
In order to trigger our matching engine in `analysis.py.score` we utilize `Celery`. It allows us to execute tasks asynchronously which means users can match at the same time and we can scale the matching easier.

#### Redis
In between `Django` and `Celery` we have `Redis` as a message broker. 
This is currently in progress and the exact way we configure it is still in progress.

#### Caddy
In the production environment we go away from using `Django` as the webserver directly. Rather traffic is first handeled by `Caddy`.
This has not been configured or tested yet and is still in progress.

#### Kubernetes
Uses a managed loadbalancer, `PostgreSQl` instance as database, managed `Redis` instance as cache,
and Spaced Object Storage for static and media files.
This has not been configured or tested yet and is still in progress.


#### Github Actions CI
For our continous integration we are using Github Actions. 
Anytime a change is to occur on the master branch we're running the functionality tests and the unit tests of the APIs.



-------------------------------

<!---
[//]: #  $$$ Sentry
[//]: #  Sentry is an error logging aggregator service. You can sign up for a free
[//]: # account at  https://sentry.io/ or download and host it yourself.
[//]: # You must set the Sentry url in production.
[//]: # -------------------------------
[//]: # $$$ Graylog
[//]: # Graylog is an log aggregation service. You need to host it yourself and set the
[//]: # graylog host in production.
[//]: # -------------------------------
--->




## Docker Commands

Since we do our entire development inside `Docker` containers, it's nice to have some often used commands ready.

#### Build the local environment:
`$ docker-compose -f compose/local.yml up --build`

#### Build the production environment
`$ docker-compose -f compose/production.yml up --build`

#### See all running containers
`$ docker ps`

#### Stop all containers:
`$ docker kill $(docker ps -q)`

#### Remove all containers in your system
`$ docker rm $(docker ps -a -q)`

#### Remove all docker images
`$ docker rmi -f $(docker images -q)`

#### Remove all docker volumes
`$ docker volume ls -qf dangling=true | xargs  docker volume rm`

#### Login to container, get processing_id from docker ps
`$ docker exec -t -i  <processing_id> bash`

#### See error messages in building container:
`$ docker-compose -f compose/local.yml logs -f`

#### Enter Django python shell
`$ docker-compose -f compose/local.yml run django python manage.py shell`

#### Inspect a volume created
`$ docker volume inspect django-on-docker_postgres_data`

#### Make migrations for one app Landing_page
`$ docker-compose -f compose/local.yml run django python manage.py makemigrations Landing_page`

#### Make migrations for the general project
`$ docker-compose -f compose/local.yml run django python manage.py makemigrations`

#### Apply migrations
`$ docker-compose -f compose/local.yml run django python manage.py migrate`

#### Revert migrations
`$ docker-compose -f compose/local.yml run django python manage.py migrate Landing_page zero`

#### Create Admin users:
`$ docker-compose -f compose/local.yml run django python manage.py createsuperuser `

#### Create Django project
`$ docker-compose -f compose/local.yml exec django django-admin startproject project_name`

#### Conversion from .shp file to postGIS table (Later when we incorporate geoDjango)
`$ docker-compose -f compose/local.yml exec django ogr2ogr -f "PostgreSQL" PG:"dbname=hello_django_dev user=hello_django password=hello_django" ne_10m_populated_places.shp -nln City -append`

-------------------------------

## Database commands

#### Access database
`$ docker-compose -f compose/local.yml exec postgres psql --username=apartmenthelper --dbname=apartmenthelper`

#### Drop Database
`$ docker exec -it apartmenthelper_local_postgres_id psql -U apartmenthelper -d postgres -c "DROP DATABASE apartmenthelper;"`

#### Get all the existing tables inside the database
`$ \dt`

#### Get all data from table (Note the quotations on the table name)
`$ select * from "Landing_page_user";`

#### Remove all of the user data
`$ truncate table "Landing_page_user" cascade;`

-------------------------------

## Django testing

#### Run the django tests
`$ docker-compose -f compose/local.yml run django coverage run --source=apartmenthelper manage.py test`

#### Get a coverage report of the django tests
`$ docker-compose -f compose/local.yml run django coverage report`

-------------------------------

## API Usage

We have several APIs to access the data in the backend.
If you want to have an overview of them you can access them through swagger on your local system if you have the `django` docker container running:
http://127.0.0.1:8000/api-docs/

### Examples of usage

Most notably we have the registration and login APIs.
To use them we need to send a http request to their respective urls with the data in a json structure.

For example using the curl command found on mac and some linux systems:
`$ curl -d '{
    "email": "admin@email.com",
    "password1": "adminuser123",
    "password2": "adminuser123",
    "first_name": "admin",
    "last_name": "user"
}' -H 'Content-Type: application/json' http://127.0.0.1:8000/api/v1/rest-auth/registration/`

That command sends the data to the API registration page and an verification email is sent to the user.



