#!/usr/bin/python3
"""
    prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
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

    state = session.query(State.id).where(State.name == args[4]).first()

    if state:
        print(state[0])
    else:
        print("Not found")
