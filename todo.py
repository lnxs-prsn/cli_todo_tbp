import argparse
import datetime
import json
import os

# this function creates an task and stores it to json file
def add_task():
    parser = argparse.ArgumentParser(description='cli todo')

    parser.add_argument('task_name', type=str, help='write the title of the task')
    parser.add_argument('task_description', type=str, help='write task description')
    parser.add_argument('end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='write end date of the task example format 2025-08-30',)
    
    args = parser.parse_args()
    # lines below create file and store to the file the tasks 
    print(args.task_name, args.task_description, args.end_date)
    with open('./cli_todo.json', 'w', encoding='utf-8') as ff:
        json.dump({f'{args.task_name}':{'task_name':f'{args.task_name}', 'task_description':f'{args.task_description}', 'end_date':f'{args.end_date}'}}, ff)

# add_task()

# this function opens the json file and print data on the file to terminal
def edit_task():
    data = {}
    if os.path.exists('./cli_todo.json'):
        try:

            with open('./cli_todo.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            size = os.path.getsize('./cli_todo.json')
            if size == 0:
                print('file is empty')
            data = {}
    else:
        print('no such a file')


    # data['buy milk']['task_description'] = 'get milk from shop3'
    # print(data['task_name']['task_description'])
  
    for x,y in data.items():
        print(x, y)


edit_task()