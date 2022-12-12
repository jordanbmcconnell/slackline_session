from .core import db
from flask_security import (
    SQLAlchemyUserDatastore, UserMixin, RoleMixin)
from sqlalchemy import func


class Trick(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    created_on = db.Column(db.DateTime(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
