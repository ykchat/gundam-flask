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

    url = 'mongodb://' + config['mongodb']['host'] + '/gundam_flask'

    client = MongoClient(url)
    db = client.get_default_database()

    api.add_resource(HelloWorld, '/api/ping')
    api.add_resource(Mobilesuits, '/api/v1/mobilesuits', resource_class_kwargs={'db': db})
    api.add_resource(Mobilesuit, '/api/v1/mobilesuits/<string:_id>', resource_class_kwargs={'db': db})

    app.run(host='0.0.0.0', port=port, debug=True)
