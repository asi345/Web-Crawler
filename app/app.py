## @mainpage Main Page
# @author İsmail Ata İnan
# @brief A Docker project that allows web crawling using a website interface
## @section Introduction
# This project is made for UITSEC company, which is a company working on cyber security
# technologies. It is a Docker project which allows it to be used in many platforms. It allows
# users to gain information about websites by doing web crawling. It is implemented like a
# website, so the project can be accessed using any web browser after it is run. The project in
# general takes inputs from user in the web page, does web crawling in the given web page using
# some code in Python, saves the information it gathers from the webpage in a database server,
# then displays the resulting records in the webpage using the data in the database.
## @section Core Core of the System
# In this Docker project, there are 3 containers to be run. They are Flask, MongoDB and Nginx
# images. Flask serves as a web application development interface in Python. MongoDB is our
# NoSQL database. Nginx is the webserver hosting program. Thus, Nginx image is connected to
# Flask image, Flask image is connected to both Nginx and MongoDB images and MongoDB image is
# connected to Flask image. Docker is the whole system maintaining these images and isolating
# them from the outside processes and files.

## @file app.py
# @author İsmail Ata İnan
# @brief Implementation of the Flask application of the Web Crawler

import os
from flask import Flask, request, render_template, url_for, flash, redirect
import requests
from bs4 import BeautifulSoup
from flask_pymongo import PyMongo
from datetime import datetime

## @brief Flask web application object
application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

## @brief Connects web application to the Mongo database
mongo = PyMongo(application)

## @brief crawling_histories table in the database which will be listed in the website
# crawling_histories = address id, url, parent id, crawling date and time, number of links in the website, how many of these links are inserted into the database
infos = mongo.db.crawling_histories

## @brief Current available address ID in the database to be used for storing the next url
globalid = 0

## @param url The url of the website to be crawled
# @param parentid The ID of the website which calls the current website
# @brief Goes to the website with the given url, extracts some information about it, stores them
# in the database and recursively goes all the website links contained in this website. The
# extracted information about websites include unique address id, website url, parent website
# id, crawling date and time, number of links in the website and how many of these links are
# inserted into the database.
def linker(url, parentid=-1) :

    global globalid

    try :
        page = requests.get(url).text
    except :
        return
    
    found = infos.find_one({"url" : url})

    if found :
        #curid = found["id"]
        return
    else :
        curid = globalid
        globalid += 1

    moment = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

    soup = BeautifulSoup(page, "html.parser")
    links = [link.get("href") for link in soup("a")]
    
    item = {"id" : curid, "url" : url, "parent_id" : parentid, "datetime" : moment, "noflinks" :
            len(links), "newinserts" : 0}
    infos.insert_one(item)

    parent = infos.find_one({"id" : parentid})
    if parent :
        updated = {"$set": {"newinserts" : parent["newinserts"] + 1}}
        infos.update_one(parent, updated)

    for link in links : 
        linker(link, curid)

## @brief The main and only page of the web application. It has a input text area and submission
# button for taking input urls from the application user. Then it has a table showing the
# whole crawling_histories database records.
@application.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST" :
        url = request.form["URL"]
        linker(url)
        
    return render_template("index.html", infos=infos.find())

## @brief The running setup of the web application. It specifies the local IP address which the
# application will run on and environment variables and arguments to set up a stable and
# responsive application.
if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
