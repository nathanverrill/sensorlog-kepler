# Mapping Sensorlog Data in Kepler

Nathan Verrill, SAIC, nathan.verrill@saic.com

14 Oct 2022

## TL/DR
* Place `json` from sensorlog in `data/`
* Load data `python3 kepler-prep.py`
* Launch map `flask run --reload --host=0.0.0.0 --port=80`
* Activate timeline in `Filters` > `Sensorlog Dataset` > `timestamp`

## TODO
* Read multiple log files
* Request conversion through API
* Retreive data from API
* API caching
* Request filtering (geofence, time, label)

## Overview

Display Sensorlog data in a Kepler map using Flask. Map runs at `localhost:80` unless otherwise specified when running.

All sensor data is included as `properties` in the `Geojson` feature collection and are automatically available in Kepler with full visualization and filtering capabilities.

## Setup
* `python3 -m venv env`
* `source env/bin/activate`
* `python3 -m pip install --upgrade pip`
* `python3 -m pip install -r requirements.txt`
* `export FLASK_APP=kepler-flask.py`

## Prep Geojson
* Place sensorlog data in JSON format named `sensorlog.json` in `./data` folder
* Generate Geojson: `python3 kepler-prep.py`
* You should now see a file in the data folder called `sensorlog_geojson_features.json`
* The features json file is automatically loaded in Kepler
* Re-run script at any time. 
* Existing will be overwritten. To append, update `kepler-prep.py` and change the `w` to `a` in `with open`

## Running Map
* `flask run --reload --host=0.0.0.0 --port=80`
* Update host and port to your needs
* Turn on timeline replay by going to `Filters`, choosing the `sensorlog` dataset, and the `timestamp` field

### How it works
* The Kepler map loads `data/sensorlog_geojson_features.json` and loads map automatically
* Map centers on SAIC headquarters
* Default map settings can be updated in the config variable in `kepler-flask.py`
* The Geojson contains all Sensorlog fields as `properties` that can be used for analysis in Kepler, including animation, filters, and other visualizations.