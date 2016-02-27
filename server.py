#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import yaml
import json
from flask import Flask
from flask.ext.cors import CORS
from flask_restful import Resource, Api
from pymongo import MongoClient
from resources.v1.mobilesuit import Mobilesuit, Mobilesuits

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'gundam'}

if __name__ == '__main__':

    app = Flask(__name__)
    CORS(app)

    api = Api(app)

    config = yaml.load(file('./config/server.yml'))['server']

    port = config['port']
    # for Cloud Foundry
    port = int(os.getenv('PORT', port))

    mongodb_url = ''
    if 'VCAP_SERVICES' in os.environ:
        # for Cloud Foundry
        services = json.loads(os.environ['VCAP_SERVICES'])
        mongodb_url = services['mongolab'][0]['credentials']['uri']
    else:
        mongodb_host = config['mongodb']['host']
        # for Docker link
        mongodb_host = os.getenv('MONGO_PORT_27017_TCP_ADDR', mongodb_host)
        mongodb_url = "mongodb://%s/gundam_flask" % (mongodb_host)

    client = MongoClient(mongodb_url)
    db = client.get_default_database()

    api.add_resource(HelloWorld, '/api/ping')
    api.add_resource(Mobilesuits, '/api/v1/mobilesuits', resource_class_kwargs={'db': db})
    api.add_resource(Mobilesuit, '/api/v1/mobilesuits/<string:_id>', resource_class_kwargs={'db': db})

    app.run(host='0.0.0.0', port=port, debug=True)
