#Trying to create an API to rollback our applications

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import astapp = Flask(__name__)
import os

api = Api(app)

class Users(Resource):
    # do the roll back with keyword
    # methods go here
    pass
class Locations(Resource):
    # methods go here
    pass

api.add_resource(Users, '/users') # '/users' is our entrypoint
api.add_resource(Locations, '/locations') # '/locations' is our entrypoint

path = '/home/ansible/vpn_ops'
files = os.listdir(path)

for file in files:
    print(file)

if __name__ == '__main__':
    app.run() # Run our Falsk app