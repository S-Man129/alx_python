#!/usr/bin/python3

# Import necessary modules and classes
import sys                 # Import the sys module to access command-line arguments
from model_state import Base, State  # Import the Base and State classes from model_state
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy

if __name__ == "__main__":
    # Create an SQLAlchemy engine to connect to the database
    # The provided arguments are assumed to be: username, password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create the tables in the database based on the defined models (declarative_base)
    Base.metadata.create_all(engine)
