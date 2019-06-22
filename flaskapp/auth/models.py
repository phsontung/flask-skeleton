from flask_login import UserMixin

from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    login_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}>'.format(self.email)


# class UserToken(db.Model):
#     id = db.Column(db.)
