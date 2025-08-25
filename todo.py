import argparse
import datetime
import json


def add_task():
    parser = argparse.ArgumentParser(description='cli todo')

    parser.add_argument('task_name', type=str, help='write the title of the task')
    parser.add_argument('task_description', type=str, help='write task description')
    parser.add_argument('end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='write end date of the task',)
    
    args = parser.parse_args()
    
    print(args.task_name, args.task_description, args.end_date)
    with open('./cli_todo.json', 'w', encoding='utf-8') as ff:
        json.dump({'task_name':f'{args.task_name}', 'task_description':f'{args.task_description}', 'end_date':f'{args.end_date}'}, ff)

# add_task()


def edit_task():
    with open('./cli_todo.json', 'r') as file:
        data= json.load(file)
    print(data)


edit_task()