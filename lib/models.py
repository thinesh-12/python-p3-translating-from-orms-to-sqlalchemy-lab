#!/usr/bin/env python3
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base




class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())


# if __name__ == "__main__":
#     engine = create_engine("sqlite:///:dogs:")
#     Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()