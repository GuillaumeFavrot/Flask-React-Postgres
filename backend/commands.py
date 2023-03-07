#!/bin/python

from backend.exts import db
from backend.app import app

def create_all ():
    with app.app_context():
        db.create_all()

create_all()