#!/bin/python
import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from backend.config import Config, static_folder_path
from backend.exts import db
from backend.views import routes

# Application initialization
# The two arguments after the __name__ are responsible for Flask correct handling of React static files
app = Flask(__name__, static_url_path='', static_folder=static_folder_path)
app.register_blueprint(routes)
app.config.from_object(Config)

# Production DB URI (comment while on devloppement)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/db.sqlite'

# Developpement DB URI (comment while on production)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
db.init_app(app)

#Comment this on deployment
CORS(app) 
 
# # Run server
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000)