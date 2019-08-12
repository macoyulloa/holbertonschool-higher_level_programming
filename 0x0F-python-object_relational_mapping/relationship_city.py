#!/usr/bin/python3
'ORM project'
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    ' class definition inherits from Base '
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
