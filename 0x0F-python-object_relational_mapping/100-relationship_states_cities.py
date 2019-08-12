#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ins_state = State(name="California")
    ins_city = City(name="San Francisco")
    ins_city.state = ins_state 
    session.add(ins_state)
    session.add(ins_city) 
    session.commit()
    session.close()
