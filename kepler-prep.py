# usage 
# assumes json file in a data/ folder
# python3 kepler-prep.py
# generates geojson feature collection for use in Kepler
import json
import pickle

# sensorlog entry to geojson features
json_data = [] 

# create a geojson feature collection
# a feature collection groups a set of points for the kepler map
# the geojson is automatically parsed by kelper
featureCollection = {}
featureCollection['type'] = "FeatureCollection"
featureCollection['features'] = []
    
# to load multiple json files use glob and loop
with open('data/sensorlog.json') as json_file:
    json_data = json.load(json_file)

for entry in json_data:

    geometry = {}
    geometry['type'] = 'Point'
    
    # IMPORTANT geojson lists longitude (easting) first
    geometry['coordinates'] = [entry['locationLongitude'],entry['locationLatitude']]

    # Now construct a geojson feature out of the sensorlog log entry
    # Assigning the log entry JSON to the feature properties automatically
    # populates sensorlog in Kepler as plotting / filtering variables
    feature = {}
    feature['type'] = 'Feature'
    feature['geometry'] = geometry

    # add timestamp that is easy to find
    entry['timestamp'] = entry['loggingTime']
    feature['properties'] = entry

    featureCollection['features'].append(feature)

with open('data/sensorlog_geojson_features.json', 'w') as f:
    json.dump(featureCollection, f)
