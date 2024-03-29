# Importing modules including Flask
import numpy as np
import os
import datetime as dt

#Reflect Tables into SQLAlchemy ORM
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setting up engine to connect to database

engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Generating app name and defining routes
app = Flask(__name__)
@app.route("/")
def all()
    return (
        f'Routes available:<br>'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/station<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/startdate<br/>'
        f'/api/v1.0/enddate<br/>'

    )