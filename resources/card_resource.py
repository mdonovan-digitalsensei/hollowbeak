from flask_restful import Resource
from flask import request
from models.card_model import CardModel
from marshmallow import ValidationError

from schemas.card_schema import CardSchema

card_schema = CardSchema()


class Card(Resource):
    def get(self, card_id):
        card = CardModel.find_by_id(card_id)

        if not card:
            return {"message": "card not found"}, 404
        return card_schema.dump(card), 200

    def post(self, card_id):
        try:
            card = card_schema.load(request.json)
        except ValidationError as err:
            return err.messages, 400
        try:
            card.save_to_db()
        except:
            return {"message": "Error inserting"}, 500

        return card_schema.dump(card), 201
