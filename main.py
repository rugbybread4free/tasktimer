import time
import datetime
from blessed import Terminal
import json
from functions import *

term = Terminal()





#print(str(datetime.timedelta(seconds =end -start)))






#json data[level1][level2]
#1. read json file 2. process 3. write/update json

def create_json():
    data = {
        'projects':{
            'project_name':{ #This is the title of the project, to fetch title, fetch this key
                'total_elapsed_time':0,
                'description':'something desc',
                'session':[
                    #each logged session will be added as an dict item in the list with property of start time and length
                    {
                        'start_time':0,
                        'session_length':0
                    }
                    ]
                }
            }
        }

    with open('save.json', 'w') as datafile:
        json.dump(data, datafile, indent=4)

#create_json() #will recreate the save file - running this will erase existing data!





while True:
    term.clear()

    print(term.darkorange2("1. (N)ew project \n2. (L)oad existing project \n3. (P)roject options"))
    choice = input()
    if choice in ['1', 'n', 'N', 'New', 'new']:
        new_project()
        pass
    elif choice in ['2', 'l', 'L', 'load', 'Load']:
        name = load_project()
        #timer(name)
    elif choice in ['3', 'p', 'P', 'options', 'Options']:
        edit_projects()
        pass