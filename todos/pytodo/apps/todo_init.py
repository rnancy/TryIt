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


deadline = datetime.strptime('2018-03-30', '%Y-%m-%d') 
new_project = Project(name='DBAutomation', description="rundeck, puppet", deadline =deadline)
session.add(new_project)
session.commit()
session.query(Project).all()
while(True):
    # cntrl-c to quit
    input = raw_input('todo$ ')

    process = subprocess.Popen(input, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    out, err = process.communicate()

    print(out)
    print(err)
