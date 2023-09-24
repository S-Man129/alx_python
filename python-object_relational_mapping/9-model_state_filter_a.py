import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if three command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract the command-line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Define the MySQL database connection URL
    db_url = f'mysql://{username}:{password}@localhost:3306/{database_name}'

    # Create the database engine
    engine = create_engine(db_url, echo=False)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all State objects containing 'a'
    session_state = session.query(State)
    states = session_state.filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
