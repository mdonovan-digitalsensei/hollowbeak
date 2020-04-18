from flask_restful import Resource, reqparse
from models.card_model import CardModel


class Card(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "title", type=str, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "is_done", type=bool, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "schedule", type=int, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "board_id", type=int, required=True, help="This field cannot be left blank!"
    )

    def get(self, card_id):
        card = CardModel.find_by_id(card_id)
        if card:
            return card.json()

    def post(self):
        data = Card.parser.parse_args()
        card = CardModel(data["title"], data["is_done"], data["schedule"], data["board_id"])
        card.save_to_db()
        return card.json(), 201
