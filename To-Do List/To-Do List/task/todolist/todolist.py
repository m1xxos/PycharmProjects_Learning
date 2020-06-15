# Write your code here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

start_string = """\n1) Today's tasks
2) Add task
0) Exit
"""

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def add_task(task, date='01-24-2020'):
    new_row = Table(task=task)
                    # deadline=datetime.today())
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def today_task():
    print("Today:")
    rows = session.query(Table).all()
    if rows:
        for tasks in rows:
            print(tasks.id, end=". ")
            print(tasks.task)
    else:
        print("Nothing to do!")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
while True:
    print(start_string)
    action = int(input())
    if action == 1:
        today_task()
    elif action == 2:
        print("Enter task")
        add_task(input())
    elif action == 0:
        break
print("Bye!")
