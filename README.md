# WEB CRAWLER

## General Information

This is a web application that uses a REST-API. The application runs on **Flask** in **Python3.9**, uses
**Nginx** webserver to host the application and uses **MongoDB** as database in the backend. The
whole project is isolated as an application in Docker. So Docker is required to run this project. In
Docker, there are 3 containers for this project: Flask, mongo and nginx. **Dockerfile**s and
**docker-compose.yml** file is configured to install images and connect these containers.

The **Doxygen** documentation for Flask part of the project can be found in **html** folder. There,
start **index.html** file to open the documentation in your default web browser.

## Installation

Firstly, [Docker](https://www.docker.com) and [Docker-Compose](https://docs.docker.com/compose/install/) is necessary since this is a Docker project. You can find the download links from the links and follow the setup procedures. After installing Docker, make sure the command ***docker*** and ***docker-compose*** is in the path.

## Run the Project

To start the project, download this repository by

    git clone https://github.com/asi345/Web-Crawler

Then, head to the project directory by

    cd Web-Crawler

We are now in our Docker project. Build the project here by

    docker-compose build

This may take a while sinceit will download and install all requirements for the project and get
the project ready for execution. Now start the containers by the command

    docker-compose up -d

This will run all the images installed in the build command. **-d** option allows the project run in
the background so we can continue to configure project settings. The execution is started, but
**Mongo** image is not connected to the database in the current configuration. We need to manually
authenticate and initialize the Mongo database. To do this, first start the **mongo** interactive
shell in the Docker by the command

    docker exec -it websearcher_mongodb_1 bash

Now the mongo interactive shell is started. Here, log in to the database by using the command

    mongo -u atabase -p

Shell now should ask for password here. The password is the same as the username, so just write

    atabase

We just logged in to the account and should head to the project database. The project is configured
to use the database named **flaskdb**, so in the current account shell write the command

    use flaskdb

to connect to the database. Here, a user is required as the user of the database with given
permissions. Create a user with the same username and password of **mongo** by the query

    db.createUser({user: 'atabase', pwd: 'atabase', roles: [{role: 'readWrite', db: 'flaskdb'}]})

This query is self explanatory, but just let me tell that it creates a new user with given
credential. It has only permission to read from and write to the **flaskdb** database. But we need
more permission to handle the database in Docker and Flask application. So to give more permission
execute the command

    db.grantRolesToUser('atabase',[{ role: "dbAdmin", db: "flaskdb" }])

After, this command, the database is authenticated and initialized. The project is now ready for
use. Open your web browser and go to the IP address **0.0.0.0**. The web application page should
load there.
