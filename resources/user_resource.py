from flask_restful import Resource
from flask import request

from models.user_model import UserModel

from schemas.user_schema import UserSchema

from marshmallow import ValidationError

user_schema=UserSchema()


class UserRegister(Resource):
    def post(self):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(user.username):
            return {"message": "User already exists"}, 400

        user.save_to_db()

        return {"message": "User created successfully"}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user.delete()
        return {"message", "User deleted"}, 200



