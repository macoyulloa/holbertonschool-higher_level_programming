#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id)
    for states in first.filter(State.name.like('%a%')).all():
        print("{}: {}".format(states.id, states.name))
    session.close()
