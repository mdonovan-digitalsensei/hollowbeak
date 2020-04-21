from marshmallow import Schema, fields


class CardSchema(Schema):
    class Meta:
        dump_only = ("id",)

    id = fields.Int()
    title = fields.Str(required=True)
    is_done = fields.Bool(required=True)
    schedule = fields.Int(required=True)
    board_id = fields.Int(required=True)
