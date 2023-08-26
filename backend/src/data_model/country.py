from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


from backend.src.data_model import country_table_name
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(Base):
    __tablename__ = country_table_name

    id = Column(Integer, primary_key=True)
    code = Column(String(2), unique=True, nullable=False)
    name = Column(String(50), unique=True, nullable=False)


# class CountrySchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Country
#         include_relationships = True
#         load_instance = True
