
from datetime import date
import os

#Calendario: dia de hoje 
datetoday = date.today()

if 'task.txt' not in os.listdir('.'):
    with open("task.txt",'w') as f:
        f.write("")

def get_task():
    with open("task.txt",'r') as f:
        task_list = f.readlines()
    return task_list

def create_task():
    os.remove("task.txt")
    with open("task.txt",'w') as f:
        f.write("")

def update_task(task_list):
    os.remove("task.txt")
    with open("task.txt",'w') as f:
        f.writelines(task_list)

