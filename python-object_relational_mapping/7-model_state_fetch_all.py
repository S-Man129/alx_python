#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if three command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <database>")
        sys.exit(1)

    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Define the MySQL database connection URL
    db_url = f'mysql://{username}:{password}@localhost:3306/{database_name}'

    # Create the database engine
    engine = create_engine(db_url, echo=False)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all State objects and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
