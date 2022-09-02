#Trying to create an API to rollback our applications

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os

app = Flask(__name__28)
api = Api(app)

class Users(Resource):
    # do the roll back with keyword
    # methods go here
    pass
class Locations(Resource):
    # methods go here
    pass

api.add_resource(Users, '/rollback') # '/rollback' is our entrypoint

path = '/home/ansible/'
files = os.listdir(path)

for file in files:
    print(file)

if __name__ == '__main__':
    app.run() # Run our Falsk app
