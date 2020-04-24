from ma import ma
from models.card_model import CardModel
from models.board_model import BoardModel


class CardSchema(ma.ModelSchema):

    class Meta:
        model = CardModel
        dump_only = ("id",)
        include_fk = True