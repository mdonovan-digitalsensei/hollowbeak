from db import db


class BoardModel(db.Model):
    __tablename__ = "boards"
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cards = db.relationship('CardModel', lazy='dynamic')
    user = db.relationship('UserModel')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, board):
        return cls.query.filter_by(title=board).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
