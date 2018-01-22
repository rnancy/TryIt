import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Project(Base):
    __tablename__ = 'project'
    # Here we define columns for the table project
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(30), primary_key=True)
    description = Column(String(250), nullable=False)
    deadline = Column(Date, nullable=False)
 
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    priority = Column(Integer, default=1)
    status = Column(String(12), nullable=False)
    details = Column(String(250), nullable=False)
    deadline = Column(Date, nullable=False)
    completed_on =  Column(Date, nullable=False)
    project = Column(String(30), ForeignKey('project.name'), nullable = False)

    project = relationship(Project)
 

def init_todo_db (engine, Base):

     # Create an engine that stores data in the local directory's
     # todo.db file.
     engine = create_engine('sqlite:///todo.db')
 
     # Create all tables in the engine. This is equivalent 
     # to "Create Table"
     # statements in raw SQL.
     Base.metadata.create_all(engine)
