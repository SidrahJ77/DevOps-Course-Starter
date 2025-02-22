# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

# Setting Up The Mongo DB Database

This app uses a Mongo DB Database for storing the todo items. You'll need to set up:
* A Mongo DB Account and Database
* Provide a connection string to connecting to said database

Once you have done this then you'll need to update the `.env` fileto include your Mongo DB Database details.

## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Test Suite
To run the test for the codebase run the following command:
```
Poetry run pytest
```
(please make usre you run 'poetry install' beforehand to install 'pytest')

If intead you would like to run your tests via Docker, please run the followig:
```
docker build --tag todo-app:test --target test .
docker run todo-app:test
```

## Building and Running the App via Docker
To build the container for local development, please run
```bash
docker build --tag todo-app:dev --target development .
```
To run the container for local development, please run
```bash
docker run --publish 8000:5000 -it --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```
For the production container, the build and run commands are:
```bash
docker build --tag todo-app:prod --target production .
docker run --publish 8000:5000 -it --env-file .env todo-app:prod
```

## Images are stored in 'Diagrams' folder

## Azure Hosting
The container image that is deployed to Azure is hosted on Docker Hub at: https://hub.docker.com/repository/docker/sidrahj/hello-world/general

The website itself is hosted at: https://sidrahsappservice.azurewebsites.net/

To update the website you will need to run the following commands:
```
docker build --tag sidrahj/hello-world --target production .
docker push sidrahj/hello-world
```

Next you'll need to make a POST request to the webhook link provided on the App Service (under the Deployment Centre tab). This will trigger Azure to pull the updated image from Docker Hub.