import argparse
import datetime
import json
import os



# this function creates an task and stores it to json file
def add_task(task_name, task_description, end_date, **args):
    # args = parser.parse_args() delete later
    # lines below create file and store to the file the tasks 
    if os.path.exists('./cli_todo.json') and os.path.getsize('./cli_todo.json')!=0:
        print('file exists already')
        print(os.path.getsize('./cli_todo.json'))
        with open('./cli_todo.json', 'r', encoding='utf-8') as fa:
            data = json.load(fa)
            task = {'task_name':f'{task_name}', 'task_description':f'{task_description}', 'end_date':f'{end_date}'}
            data.append(task)
            print(data)
        with open('./cli_todo.json', 'w', encoding='utf-8') as fs:
            # json(data)
            print(data)
            json.dump(data, fs)
            pass
            
    else:
        # print(args.task_name, args.task_description, args.end_date)
        with open('./cli_todo.json', 'w', encoding='utf-8') as ff:
            task = [{'task_name':f'{task_name}', 'task_description':f'{task_description}', 'end_date':f'{end_date}'},]
            # print(task)
            json.dump(task, ff)


# this function opens the json file and print data on the file to terminal
def edit_task(task_name=None, task_description=None, end_date=None):
    # parser = argparse.ArgumentParser(description='cli todo') delete later
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

    print(task_name)
    task = {}
    for x in data:
        for a,s in x.items():
            if task_name in s:
                task = x


    # functionality to edit the tasks

    if task_description != None:
        task['task_description'] = task_description
    else:
        pass
    if end_date != None:
        task['end_date'] = end_date.strftime('%Y-%m-%d')

    else:
        pass

    # writes edited tasks back to json file

    with open('./cli_todo.json', 'w') as file:
        json.dump(data, file)


def delete_task(args):
    print('hello from del')
    if os.path.exists('./cli_todo.json', 'r', encoding='utf-8') as ff:
        try:
            pass
    pass 


def task_list(args):
    print('hello')

    if os.path.exists('./cli_todo.json'):
        try:
            with open('./cli_todo.json', 'r', encoding='utf-8') as ff:
                data = json.load(ff)
        except json.JSONDecodeError:
            size = os.path.getsize('./cli_todo.json')
            if size == 0:
                print('file is empty')


    for x in data:
        print(x)
    pass

def done_task():
    pass 



def main():
        
    parser = argparse.ArgumentParser(description='cli todo')
    subparser = parser.add_subparsers(help='subcommand help')

    # add functionality
    parser_add_task = subparser.add_parser('add', help='add task')
    parser_add_task.set_defaults(func=lambda args: add_task(args.task_name, args.task_description, args.end_date))

    parser_add_task.add_argument('task_name', type=str, help='write the title of the task')
    parser_add_task.add_argument('task_description', type=str, help='write task description')
    parser_add_task.add_argument('end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='write end date of the task example format 2025-08-30',)
        


    # editing functionality
    parser_edit_task = subparser.add_parser('edit',help='edit tasks')
    parser_edit_task.set_defaults(func= lambda args: edit_task(args.task_name, args.task_description, args.end_date))
    parser_edit_task.add_argument('--tname', type=str, dest='task_name', help='write the title of the task you want to edit')
    parser_edit_task.add_argument('--desc', type=str, dest='task_description', help='edit task description')
    parser_edit_task.add_argument('--end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='edit end date of the task example format 2025-08-30', dest='end_date')


    # list functionality
    parser_task_list = subparser.add_parser('list', help='task list')
    parser_task_list.set_defaults(func=task_list)


    # delete task functionality
    parser_delete_task = subparser.add_parser('del', help='delete task')
    parser_delete_task.set_defaults(func=delete_task)





    # all the arguments from the cli
    args = parser.parse_args()
    # args.func(args.task_name, args.task_description, args.end_date)
    args.func(args)

    # functions
    # add_task(args.task_name, args.task_description, args.end_date)

    # edit_task(args.task_name, args.task_description, args.end_date)



main()