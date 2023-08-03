#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).filter(State.name == sys.argv[4]).first()
    if row:
        print(row.id)
    else:
        print("Not found")
    session.close()
