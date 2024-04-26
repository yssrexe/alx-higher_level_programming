#!/usr/bin/python3
"""
    prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # ---------- method 1 ----------
    # results = session.query(State, City).join(
    #     City, State.id == City.state_id).order_by(City.id).all()

    # for res in results:
    #     print(f"{res[0].name}: ({res[1].id}) {res[1].name}")

    # ---------- method 2 ----------
    cities = session.query(City).order_by(City.id)
    if cities:
        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")
