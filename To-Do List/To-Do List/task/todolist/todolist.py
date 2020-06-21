# Write your code here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

start_string = """\n1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def convertdate(dstring):
    return datetime.strptime(dstring, '%Y-%m-%d')


def add_task():
    print("Enter task")
    task = input()
    print("Enter deadline")
    date = convertdate(input())
    new_row = Table(task=task, deadline=date.date())
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def show_tasks(day):
    rows = session.query(Table).all()
    tsks = 0
    if rows:
        for tasks in rows:
            if tasks.deadline == day.date():
                tsks += 1
                print(tsks, end=". ")
                print(tasks.task)
    if tsks == 0:
        print("Nothing to do!")


def today_task():
    today = datetime.today()
    print(f"Today {today.day} {today.strftime('%b')}")
    rows = session.query(Table).all()
    tsks = 0
    if rows:
        for tasks in rows:
            if tasks.deadline == datetime.today().date():
                tsks += 1
                print(tsks, end=". ")
                print(tasks.task)
    else:
        print("Nothing to do!")
    if tsks == 0:
        print("Nothing to do!")


def week_tasks():
    today = datetime.today()
    for i in range(0, 7):
        day = today + timedelta(days=i)
        print(f"\n{week[day.weekday()]} {day.day} {day.strftime('%b')}:")
        show_tasks(day)


def all_tasks():
    print('All tasks:')
    rows = session.query(Table).all()
    session.query(Table).order_by(Table.deadline)
    tsks = 0
    if rows:
        for tasks in rows:
            tsks += 1
            print(tsks, end=". ")
            print(tasks.task, end=". ")
            print(f"{tasks.deadline.day} {tasks.deadline.strftime('%b')}")
    else:
        print("Nothing to do!")


def show_missed():
    print('Missed tasks:')
    tsks = 0
    rows = session.query(Table).filter(Table.deadline < datetime.today()).all()
    if rows:
        for tasks in rows:
            tsks += 1
            print(tsks, end=". ")
            print(tasks.task, end=". ")
            print(f"{tasks.deadline.day} {tasks.deadline.strftime('%b')}")
    else:
        print("No missed tasks")


def delete_task():
    rows = session.query(Table).all()
    tsks = 0
    if rows:
        print('Chose the number of the task you want to delete:')
        for tasks in rows:
            tsks += 1
            tasks.id = tsks
            print(tsks, end=". ")
            print(tasks.task, end=". ")
            print(f"{tasks.deadline.day} {tasks.deadline.strftime('%b')}")
        id = int(input())
        session.query(Table).filter(Table.id == id).delete()
        session.commit()
    else:
        print("Nothing to delete!")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
while True:
    print(start_string)
    action = int(input())
    if action == 1:
        today_task()
    elif action == 2:
        week_tasks()
    elif action == 3:
        all_tasks()
    elif action == 4:
        show_missed()
    elif action == 5:
        add_task()
    elif action == 6:
        delete_task()
    elif action == 0:
        break
print("Bye!")
