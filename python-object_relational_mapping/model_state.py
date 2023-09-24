#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

# Example usage:
if __name__ == '__main__':
    from sqlalchemy import create_engine

    # Create an SQLAlchemy engine and bind it to the MySQL database
    engine = create_engine('mysql://username:password@localhost:3306/database_name')

    # Import all classes that inherit from Base before calling create_all
    Base.metadata.create_all(engine)
