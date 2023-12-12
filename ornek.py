from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self, sayi):
            sayi_int = int(sayi)
            if sayi_int < 30 :
                if sayi_int % 2 == 0:
                     url = "https://meowfacts.herokuapp.com/?count=" + sayi
                     response = requests.get(url)
                     data = response.json()
                     return {'data': data['data']}, 200
                else:
                     return {'message' : 'Please enter a even numbers.'},400
            else:
                 return {'message': 'Please enter a number less than 30.'},400

def post(self):
       name = request.args['name']
       age = request.args['age']
       city = request.args['city']
       req_data = pd.DataFrame({
           'name'      : [name],
           'age'       : [age],
           'city'      : [city]
       })

       data = pd.read_csv('users.csv')
       #data = pd.concat([data, req_data], ignore_index=True)
       data = data.append(req_data, ignore_index=True)
       data.to_csv('kullanici.csv', index=False)
       return {'message' : 'Record successfully added.'}, 201

class Cities(Resource):
    def get(self):
        data = pd.read_csv('users.csv',usecols=[2])
        data = data.to_dict('records')
        return {'data' : data}, 200

class Name(Resource):
    def get(self,name):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 400

api.add_resource(Users, '/users/<string:sayi>')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/isim/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()
