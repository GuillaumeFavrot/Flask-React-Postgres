#!/bin/python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

static_folder_path = './../frontend/build'

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False