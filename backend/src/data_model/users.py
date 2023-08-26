from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from backend import db
from backend.src.data_model import users_table_name

class Users(db.Model):
    __tablename__ = users_table_name

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)


class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True
