from flask_restful import Resource, Api
from flask import request

class SignUp(Resource):
    def get(self):
        data = request.get_json()

        try:
            username = data['username']
            password = data['password']
        except Exception:
            return {"error": "bad data"}, 400
       
        # TODO add the user to the database

        return {
           "message": "User created successfully"
        }

class Login(Resource):
    def get(self):
        # TODO handle bad data
        data = request.get_json()

        try:
            username = data['username']
            password = data['password']
        except Exception:
            return {"error": "bad data"}, 400

        return {
            "message": "User logged in successfully"
        }
