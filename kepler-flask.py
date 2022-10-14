#export FLASK_APP=kepler-flask.py
#flask run --reload --host=0.0.0.0 --port=80
from flask import Flask
import keplergl
import json
import pickle

app = Flask(__name__)

# helper functions
import glob
import json

data = None


def load_data():
    
    global data 

    if data is None:

        print('Loading data...')
        
        with open('data/sensorlog_geojson_features.json') as f:
            data = json.load(f)

        print(f'Loaded {len(data["features"])} geojson features.')

    return data


@app.route('/')
def index():

    global data

    if data is None:

        data = load_data()

    map_config = {
        "version": "v1",
        "config": {
            "mapState": {
                "dragRotate": True,
                "latitude": 38.956562464547964,
                "longitude": -77.35618416966504,
                "zoom": 11,
                "isSplit": False
            }
        }
    }


    geoMap = keplergl.KeplerGl(height=400, data={"sensorlog": data}, config=map_config)

    return geoMap._repr_html_()

if __name__ == '__main__':

    app.run(debug=True)