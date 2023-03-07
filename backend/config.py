#!/bin/python
import os

# Defines the base directory of the backend folder
basedir = os.path.abspath(os.path.dirname(__file__))

# Defines the relative location of the frontend build folder
static_folder_path = './../frontend/build'

# Object bundling DB configuration variables
class Config(object):
    """DB config class"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False