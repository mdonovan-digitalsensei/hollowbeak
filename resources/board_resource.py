from flask_restful import Resource, reqparse
from models.board_model import BoardModel


class Board(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "board", type=str, required=True, help="This field cannot be left blank!"
    )

    def get(self, board_id):
        board = BoardModel.find_by_id(board_id)
        if board:
            return board.json()
        return {'message', "Board does not exist"}, 404

    def post(self):
        data = Board.parser.parse_args()
        board = BoardModel(data["board"],)
        board.save_to_db()
        return BoardModel.json(), 201
