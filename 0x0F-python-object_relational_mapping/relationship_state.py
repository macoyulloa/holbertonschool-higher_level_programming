#!/usr/bin/python3
'ORM project'
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    ' class definition inherits from Base '
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
