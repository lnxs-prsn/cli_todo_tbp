import argparse
import datetime

list_task = []

def add_task():
    name = input('give name to task')
    description = input('what needs to be done')
    deadline = date(input('when is the deadline date.month.year'))
    done = int(input('if done write 1 or if not done write 0'))
    task = list_task.append({'title':name, 'info':description, 'date':deadline, 'complete':done})

def task_list():
    for task in list_task:
        for items in task:
            print(items)

