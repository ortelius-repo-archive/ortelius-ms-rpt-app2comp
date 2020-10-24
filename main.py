import os
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

CAPITALS = {
    'usa': ' Washington D.C',
    'uk': 'London',
    'pakistan': 'Islamabad'
}

# Capital
# shows a single captial by country and lets you add a new, delete a new and post a new
class Capitals(Resource):
    def get(self, country_name):
        if country_name not in CAPITALS:
            return {
             'message': country_name + ' not found'
            }, 404
        return CAPITALS[country_name], 200

    def delete(self, country_name):
        if country_name not in CAPITALS:
            return {
             'message': country_name + ' not found'
            }, 404
        del CAPITALS[country_name]
        return '', 204

    def post(self, country_name):
        if country_name in CAPITALS:
            return {
             'message': country_name + ' exist already'
            }, 401
        parser = reqparse.RequestParser()
        parser.add_argument('cap', required=True)
        args = parser.parse_args()
        CAPITALS[country_name] =  args['cap']
        return CAPITALS[country_name], 201

# Capitallist
# shows a list of all the existing capitals
class CapitalList(Resource):
    def get(self):
        return CAPITALS, 200

##
## Actually setup the Api resource routing here
##
api.add_resource(CapitalList, '/capitals')
api.add_resource(Capitals, '/capitals/<country_name>')


if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000)
