from flask_restful import Resource
from models.board_model import BoardModel
from flask import request
from marshmallow import ValidationError
from schemas.board_schema import BoardSchema

board_schema = BoardSchema()


class Board(Resource):
    def get(self, board_id):
        board = BoardModel.find_by_id(board_id)
        if board:
            return board_schema.dump(board)
        return {'message', "Board does not exist"}, 404


class BoardCreate(Resource):
    def post(self):
        try:
            board = board_schema.load(request.json)
        except ValidationError as err:
            return err.messages, 400
        try:
            board.save_to_db()
        except:
            return {"message": "Error inserting"}, 500

        return board_schema.dump(board), 201
