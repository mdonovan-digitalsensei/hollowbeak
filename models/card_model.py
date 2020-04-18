from db import db


class CardModel(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    is_done = db.Column(db.Boolean())
    schedule = db.Column(db.Integer())
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
    board = db.relationship('BoardModel')

    def __init__(self, title, is_done, schedule, board_id):
        self.title = title
        self.schedule = schedule
        self.is_done = is_done
        self.board_id = board_id

    def json(self):
        return {
            "title": self.title, "is_done": self.is_done, "schedule": self.schedule, "board": self.board_id
        }

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first

    @classmethod
    def find_by_id(cls, card_id):
        return cls.query.filter_by(id=card_id).first

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
