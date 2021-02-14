ApartmentHelper ===============

Getting up and running
----------------------
This project uses Docker and Docker Compose to run the local development setup.
Make sure you have those installed: https://docs.docker.com/get-docker/

Local development
^^^^^^^^^^^^^^^^^
To start the local development environment run::

    $ docker-compose -f compose/local.yml up --build

It should start right up, no configuration from your part is required. It can
take a while as all the dependencies are installed for the first time.

Go ahead and visit http://localhost:8000 and http://localhost:3000 
in your browser. The project features live reloading, any changes you make in
the code should be apparent as soon as you refresh.

To run a management command, in this case opening an interactive interpreter, run::

    $ docker-compose -f compose/local.yml run --rm django python manage.py shell

To run the django and react test suites, respectively, run::

    $ docker-compose -f compose/local.yml run --rm django python manage.py test
    $ docker-compose -f compose/local.yml run --rm django react npm test

Single-server production
^^^^^^^^^^^^^^^^^^^^^^^^
To run the project in production on a single server requires some configuration
on your part. Ensure that Docker and Docker Compose is installed on the server,
add the missing environment variables to compose/.envs/.production, and run::

    $ docker-compose -f compose/production.yml up --build --detach

Make sure to keep the compose/.envs/.production files out of version control.
The missing environment variables are primarily authentication credentials.

To run a management command, in this case ´migrate´, run::

    $ docker-compose -f compose/production.yml run --rm django python manage.py migrate

To check on the logs run::

    $ docker-compose -f compose/production.yml logs

To see how your containers are doing, and performance metrics, respectively,
run::

    $ docker-compose -f compose/production.yml ps
    $ docker stats

If you need to scale the application, run::

    $ docker-compose -f compose/production.yml up --scale django=4

Do not scale PostgreSQL, Caddy or Redis, as those are not configured to scale.
If the performance of either becomes a bottle-neck, deploy the application on
multi-server setup using Kubernetes.

Kubernetes
^^^^^^^^
Uses a managed loadbalancer, PostgreSQl instance as database, managed Redis instance as cache,
and Spaced Object Storage for static and media files.

Setup kubernetes cluster.

    $ docker build . -f docker/kubernetes/django/Dockerfile -t dharoc/cookiecutter-project-kubernetes-django

    $ docker push dharoc/cookiecutter-project-kubernetes-django

Get logs::

    $ kubectl logs <pod_name>

Run management command::

    $ kubectl exec <pod_name> -- python /app/manage.py migrate



Sentry
^^^^^^
Sentry is an error logging aggregator service. You can sign up for a free
account at  https://sentry.io/ or download and host it yourself.

You must set the Sentry url in production.



Graylog
^^^^^^
Graylog is an log aggregation service. You need to host it yourself and set the
graylog host in production.
