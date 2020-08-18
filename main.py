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
#Beginning of program


Current_Date_Formatted = datetime.datetime.today().strftime ('%d%m%Y')

print(term.home + term.clear)
print(term.enter_fullscreen)
print(term.move_y(term.height - 1))
print(term.black_on_white(term.center('TaskTimer    ' + str(Current_Date_Formatted))))
print(term.move_y(0))

while True:
    print(term.clear_eol)
    console_print("1. (N)ew project \n2. (L)oad existing project \n3. (P)roject options \n4. (Q)uit")
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
    elif choice in ['q', 'Q', 'quit', 'Quit', '4']:
        print(term.exit_fullscreen)
        exit()