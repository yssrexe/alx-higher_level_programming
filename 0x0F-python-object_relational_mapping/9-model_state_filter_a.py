#!/usr/bin/python3
"""
    lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).where(
        State.name.like("%a%")).order_by(State.id).all()

    for state in states:
        print(state.id, state.name, sep=": ")
