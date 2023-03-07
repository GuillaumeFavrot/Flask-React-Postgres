#!/bin/python
import os

from flask import Flask
from flask_cors import CORS

from backend.config import Config, static_folder_path
from backend.exts import db
from backend.views import routes

# Application initialization
# The two arguments after the __name__ are responsible for the set up the static files folder where the frontend build will be stored
app = Flask(__name__, static_url_path='', static_folder=static_folder_path)

# Allows the outsourcing of routes to the views.py file
app.register_blueprint(routes)

# Configure the app object with the DB URI set in the config.py file 
app.config.from_object(Config)

# In order to avoid circular imports the "db" object has been created in a standalone "exts" file. The following line initialize the "db" object with the "app" object
db.init_app(app)

#Comment this on deployment
CORS(app)