from marshmallow import Schema, fields


class BoardScema(Schema):
    class Meta:
        dump_only = ("id",)

    id = fields.Int()
    board = fields.Str(required=True)
