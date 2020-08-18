import json
import time
import datetime
from blessed import Terminal
import sys

term = Terminal()

def console_print(arg_string):
    print(term.orange(arg_string))


def new_project():
    name = input("Title:: ")
    description = input("Description:: ")
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        save_data['projects'].update({name:{'total_elapsed_time':0, 'description':description, 'session':[{"start_time": 0,"session_length": 0}]}})
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
    return

def load_animation():
    animation = ['|  |  | ', '/  /  /', '-  -  - ', '\\  \\  \\ ']
    anicount = 0
    with term.hidden_cursor():
        for i in range(0, 4):
            time.sleep(0.5)
            #sys.stdout.write("\r" + animation[anicount])

            print(term.center(term.orange + animation[anicount]), end="\r")
            sys.stdout.flush()
            anicount = (anicount + 1)



def timer(projectname):
    console_print("Start timer? y/n\n")

    if input() in ['y', 'Y']:
        start = time.time()
        data = 0
        print(term.center(term.orange + "Press any key to stop timer: "))

        with term.cbreak():
            val = ""
            while val.lower() == "":
                val = term.inkey(timeout=0.1)
                if not val:
                    load_animation()
                elif val:
                    print("\n")
                    print(term.center(term.bright_white + "Stopped timer!"))

            end = time.time()
            returnvalue = datetime.timedelta(seconds=end-start)
            data = returnvalue.seconds


        with open('save.json', 'r+') as savefile:
            save_data = json.load(savefile)
            temp_data = save_data['projects'][projectname]['total_elapsed_time']
            temp_data += data
            save_data['projects'][projectname]['total_elapsed_time'] = temp_data
            savefile.seek(0)
            json.dump(save_data, savefile, indent=4)
            savefile.truncate()

        try:
            console_print("You spent {} seconds on {}\n".format(data, projectname))


        except NameError:
            print('NameError!')
    else:
        pass


def load_project():
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)


    chosen_project = list_projects_with_data()

    try:
        if chosen_project:
            console_print('You selected ' + chosen_project +'\nDescription: ' +save_data['projects'][chosen_project]['description'])
            total_elapsed_time = save_data['projects'][chosen_project]['total_elapsed_time']
            console_print('Total time: '+str(datetime.timedelta(seconds=total_elapsed_time)))
    except IndexError:
        console_print("Your choice was not in the list")

    print('\n')
    timer(chosen_project)

    return chosen_project #list_of_projects[load_choice]



def list_projects():
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)

        n = 0
        list_of_projects = []
        print("\n", end="")
        for k in save_data['projects'].keys():
            n += 1
            console_print(str(n) + '. ' + k)
            list_of_projects.append(k)
        while True:#Looping giving the user choice of project to load, until valid input is given
            console_print('Select project by number (not listed key returns): ')
            try:
                choice_for_index = int(input()) - 1
                choice_of_project = list_of_projects[choice_for_index]
                return choice_of_project
                break
            except (IndexError, ValueError):
                console_print("Returning... ")
                return False


def list_projects_with_data(): #Same base as list_projects(), but also lists the project data in a colum to the right
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)

        n = 0
        list_of_projects = []
        print("\n", end="")
        for k in save_data['projects'].keys():
            n += 1
            console_print(str(n) + '. ' + k)
            list_of_projects.append(k)


            print(term.rjust('Project name: ' + k))
            print(term.rjust('Description: ' + save_data['projects'][k][
                'description']))
            total_elapsed_time = save_data['projects'][k]['total_elapsed_time']
            print(term.rjust('Total time: ' + str(datetime.timedelta(seconds=total_elapsed_time))))





        while True:#Looping giving the user choice of project to load, until valid input is given
            console_print('Select project by number: ')
            try:
                choice_for_index = int(input()) - 1
                choice_of_project = list_of_projects[choice_for_index]
                return choice_of_project
                break
            except IndexError or ValueError:
                console_print("Your choice is not in the list, Value or Indexerror")




def edit_projects():
    projectname = list_projects()
    if projectname == False:
        pass
    elif True:
        console_print('1. (D)elete project\n2. (R)eset time of project\n3. (E)dit time manually')
        choice = input()
        if choice in ['1', '1.', 'D', 'd', 'Delete', 'delete']:
            delete_project(projectname)
            pass
        elif choice in ['2', '2.', 'R', 'r', 'Reset', 'reset']:
            reset_project(projectname)
            pass
        elif choice in ['3', '3.', 'E', 'e', 'Edit', 'edit']:
            edit_time(projectname)
            pass


def reset_project(projectname):
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        print(term.bright_white(('Reseting elapsed time in ' + str(projectname) +'...')))
        save_data['projects'][projectname]['total_elapsed_time'] = 0
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
        pass



def delete_project(projectname):
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        print(term.bright_white(('Deleting ' + str(projectname) + '...')))
        print(term.clear_eol)
        del save_data['projects'][projectname]
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
        pass


def edit_time(projectname):
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        console_print('Enter the amount of time you want to add or subtract')
        minutes = int(input('Minutes::'))*60
        hours = int(input('Hours:: '))*3600
        new_data = minutes + hours
        temp_data = save_data['projects'][projectname]['total_elapsed_time']
        temp_data += new_data
        save_data['projects'][projectname]['total_elapsed_time'] = temp_data
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
        #print(term.clear_eol)