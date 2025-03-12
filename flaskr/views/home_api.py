from flask_restful import Resource
from flask import request,jsonify
from flaskr.models.user import User
from flaskr import db

class UserRegister(Resource):
    def post(self):
        print("Received Headers:", request.headers)
        print("Received Content-Type:", request.content_type)
        if request.content_type != "application/json":
            return {"message": "Content-Type must be 'application/json'"}, 415
        data=request.get_json()
        print(data)
        new_user=User(first_name=data['first_name'],last_name=data['last_name'],email=data['email'],roll_no=data['roll_no'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"user created successfully"},201)