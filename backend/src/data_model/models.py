from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


from backend.src.data_model import users_table_name
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from backend.src.data_model import country_table_name
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Users(Base):
    __tablename__ = users_table_name

    uid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)



# class UsersSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Users
#         include_relationships = True
#         load_instance = True


