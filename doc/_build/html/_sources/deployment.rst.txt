Deployment and Application Management Procedures
================================================

.. note::
   Remember to set the ``DEBUG`` variable to ``False`` in production for security and performance reasons.
   Keep sensitive environment variables (such as ``SECRET_KEY``) out of the source code.

1. Building and Running the Application
---------------------------------------

This section covers how to build the Docker image and run it locally.

1.1. Building the Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Place the ``Dockerfile`` at the project root.
- Ensure Docker Desktop is running.
- Build the image:

  .. code-block:: bash

     docker build -t thiveyasellar/oc-lettings-site:latest .

1.2. Running the Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Run the container locally:

  .. code-block:: bash

     docker run -p 8000:8000 -e SECRET_KEY=test -e DEBUG=0 thiveyasellar/oc-lettings-site:latest

- Access the app:

  ::

     http://localhost:8000


2. Managing and Publishing Docker Images
----------------------------------------

This section explains how to manage containers and push the image to Docker Hub.

2.1. Managing Containers
~~~~~~~~~~~~~~~~~~~~~~~~

- List running containers:

  .. code-block:: bash

     docker ps

- Stop a container:

  .. code-block:: bash

     docker stop <container-id>

- Remove a container:

  .. code-block:: bash

     docker rm <container-id>

2.2. Publishing to Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Log in:

  .. code-block:: bash

     docker login

- Push the image:

  .. code-block:: bash

     docker push thiveyasellar/oc-lettings-site:latest


3. Deployment, CI/CD and Monitoring
-----------------------------------

This section covers Render deployment, GitHub Actions, and Sentry.

3.1. Creating a Docker Service on Render
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create an account at ``https://render.com``.
- Create a new web service using “Docker” as the deployment type.
- Provide your Docker Hub image URL.
- Deploy from the Render dashboard.

3.2. CI/CD with GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.2.1. Repository Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Create a ``.github/workflows`` directory at the root of your project.
- Place your workflow YAML files inside.

3.2.2. Example Pipeline
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

   name: CI
   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: |
             pip install -r requirements.txt

         - name: Run tests
           run: |
             python manage.py test

3.3. Monitoring with Sentry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.3.1. Setting Up Sentry
^^^^^^^^^^^^^^^^^^^^^^^^

- Create a Sentry account and a project.
- Install the SDK:

  .. code-block:: bash

     pip install sentry-sdk

- Configure Django:

  .. code-block:: python

     import sentry_sdk
     from sentry_sdk.integrations.django import DjangoIntegration

     sentry_sdk.init(
         dsn="your_sentry_dsn_here",
         integrations=[DjangoIntegration()],
         traces_sample_rate=1.0,
         send_default_pii=True
     )

- Logging in the application

Using Python’s built-in ``logging`` module, the application captures and records important events and errors.

Example of logging usage in a Python file::

   import logging

   logger = logging.getLogger(__name__)

   # Informational message
   logger.info(f"Displaying letting id={letting_id}: {letting.title}")

   # Error message when a letting is not found
   logger.error(f"Letting id={letting_id} not found")

3.3.2. How It Works
^^^^^^^^^^^^^^^^^^^

- Sentry captures exceptions automatically.
- Errors appear in the Sentry dashboard with stack traces, environment data, and user info.
- You can enable email notifications.

