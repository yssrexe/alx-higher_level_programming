#!/usr/bin/python3
"""
    Module that defines a City class
    that represents a cities table in the database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    """
    City class that represents a cities table in the database

    Attributes:
        id (int): city id
        name (str): city name
        state_id (int): state foreignKey
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship('State', backref="cities")
