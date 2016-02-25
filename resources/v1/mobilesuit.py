#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId

class Mobilesuits(Resource):

    def __init__(self, **kwargs):  
        self.col = kwargs['db'].mobilesuits

    def get(self):
        mobilesuits = list(self.col.find())
        map(id2str, mobilesuits)
        return mobilesuits

    def post(self):
        _id = self.col.insert_one(request.json).inserted_id
        return {'_id': unicode(_id)}

class Mobilesuit(Resource):

    def __init__(self, **kwargs):  
        self.col = kwargs['db'].mobilesuits

    def get(self, _id):
        mobilesuit = self.col.find_one({'_id': ObjectId(_id)})
        id2str(mobilesuit)
        return mobilesuit

    def put(self, _id):
        self.col.update({'_id': ObjectId(_id)}, {'$set': request.json})
        return {'_id': _id}

    def delete(self, _id):
        self.col.remove({'_id': ObjectId(_id)})
        return {'_id': _id}

def id2str(item):
    item['_id'] = unicode(item['_id'])
