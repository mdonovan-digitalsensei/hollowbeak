from ma import ma
from models.board_model import BoardModel
from models.card_model import CardModel


class BoardSchema(ma.ModelSchema):
    items = ma.Nested(CardModel, many=True)

    class Meta:
        model = BoardModel
        dump_only = ("id",)
        include_fk = True
