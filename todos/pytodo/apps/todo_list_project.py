import os
import sys
import subprocess
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from todoalchemy import Project, Task, Base

engine = create_engine('sqlite:///::memory:')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Project).all()
