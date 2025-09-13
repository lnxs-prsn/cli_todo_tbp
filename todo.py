import argparse
import datetime
import json
import os



# this function creates an task and stores it to json file
def add_task(task_name, task_description, end_date):
    # args = parser.parse_args() delete later
    # lines below create file and store to the file the tasks 

    # print(args.task_name, args.task_description, args.end_date)
    with open('./cli_todo.json', 'w', encoding='utf-8') as ff:
        json.dump({f'{task_name}':{'task_name':f'{task_name}', 'task_description':f'{task_description}', 'end_date':f'{end_date}'}}, ff)


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
    inner_data = [c for b,c in data.items()]
    print(inner_data)
    # functionality to edit the tasks
    # for e,a in vars(args).items():
    #     if a==None:
    #         for r,w in data.items():
    #             for f,g in w.items():
    #                 if e==f:
    #                     print(a,g)


    # writes edited tasks back to json file
    # for x,y in data.items():
        # print(x, y)
    # with open('./cli_todo.json', 'w') as file:
    #     json.dump(data, file)


def delete_task():
    pass 


def list_task():
    pass

def done_task():
    pass 




parser = argparse.ArgumentParser(description='cli todo')
subparser = parser.add_subparsers(help='subcommand help')

# add functionality
parser_add_task = subparser.add_parser('add', help='add task')
parser_add_task.set_defaults(func=add_task)

parser_add_task.add_argument('task_name', type=str, help='write the title of the task')
parser_add_task.add_argument('task_description', type=str, help='write task description')
parser_add_task.add_argument('end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='write end date of the task example format 2025-08-30',)
    


# editing functionality
parser_edit_task = subparser.add_parser('edit',help='edit tasks')
parser_edit_task.set_defaults(func=edit_task)
parser_edit_task.add_argument('--tname', type=str, dest='task_name', help='write the title of the task')
parser_edit_task.add_argument('--desc', type=str, dest='task_description', help='write task description')
parser_edit_task.add_argument('--end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help='write end date of the task example format 2025-08-30', dest='end_date')




# all the arguments from the cli
args = parser.parse_args()
# functions
# add_task(args.task_name, args.task_description, args.end_date)

edit_task(args.task_name, args.task_description, args.end_date)



