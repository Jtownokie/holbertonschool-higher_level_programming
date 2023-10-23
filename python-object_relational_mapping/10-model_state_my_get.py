#!/usr/bin/python3
""" SQLAlchemy Script that lists the state.id that matches a name """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    search_state = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(search_state))

    if states is None:
        print("Not found")
    else:
        print("{}".format(states.id))

    session.close()
