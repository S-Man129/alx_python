from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class represents a table in the MySQL database.
    Attributes:
        id (int): An auto-generated unique identifier for the state.
        name (str): A string representing the name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# If you want to test the script, you can include the following block of code
if __name__ == '__main__':
    from sqlalchemy import create_engine

    # Define the MySQL database connection URL (replace with your credentials)
    db_url = 'mysql://username:password@localhost:3306/database_name'

    # Create the database engine and create the 'states' table
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
