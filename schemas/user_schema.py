from ma import ma
from models.user_model import UserModel
from models.board_model import BoardModel
from models.card_model import CardModel


class UserSchema(ma.ModelSchema):
    boards = ma.Nested(BoardModel, many=True)
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True

