#!/usr/bin/python3
"""
    a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    state = session.query(State).filter(State.name == newState.name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
