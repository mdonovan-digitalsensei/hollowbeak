from db import db


class CardModel(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    is_done = db.Column(db.Boolean(), nullable=False)
    schedule = db.Column(db.Integer(), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
    board = db.relationship('BoardModel')

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, card_id):
        return cls.query.filter_by(id=card_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
