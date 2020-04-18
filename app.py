from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user_resource import UserRegister
from resources.card_resource import Card


from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFCATIONS"] = False
app.secret_key = "dave"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, "/register")
api.add_resource(Card, "/card")


jwt = JWT(app, authenticate, identity)


if __name__ == "__main__":

    app.run()
