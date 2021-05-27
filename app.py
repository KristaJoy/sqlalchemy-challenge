# Import dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setups
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Create Flask routes

# Home with routes
@app.route("/")
def home():
    return (
        f"Welcome to the Climate app!<br/>"
        f"<br/>"
        f"Routes available:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date/yyyy-mm-dd<br/>"
        f"/api/v1.0/startend_date/yyyy-mm-dd/yyyy-mm-dd"
    )

# list all precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    return(jsonify(results))

# list all stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    all_stations = list(np.ravel(results))
    return(jsonify(all_stations))

# list year temperature for most active station
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    past_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station_id = 'USC00519281'
    year_temp_data = session.query(Measurement.date, Measurement.tobs)\
            .filter(Measurement.date >= past_date).filter(Measurement.station == station_id).all()
    session.close()
    return(jsonify(year_temp_data))

# list average, max, min from a start date until now
@app.route("/api/v1.0/start_date/<start_date>")
def start_date(start_date):
    session = Session(engine)
    temp_data = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs),func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date).all()
        
    session.close()
    temp_dict = {"average_temp": temp_data[0][0], "min_temp": temp_data[0][1], "max_temp": temp_data[0][2]}
    
    return(jsonify(temp_dict))

# list average, max, min from a start date until and end date
@app.route("/api/v1.0/startend_date/<start_date>/<end_date>")
def startend_date(start_date, end_date):
    session = Session(engine)
    temp_data = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs),func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    temp_dict = {"average_temp": temp_data[0][0], "min_temp": temp_data[0][1], "max_temp": temp_data[0][2]}

    return(jsonify(temp_dict))



if __name__ == "__main__":
    app.run(debug=True)
