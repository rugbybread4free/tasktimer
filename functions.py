import json
import time
import datetime



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

def timer(projectname):
    if input("Start timer? y/n") in ['y', 'Y']:
        start = time.time()
        data = 0

        while input("Press any key to stop timer: "):
            end = time.time()
            returnvalue = datetime.timedelta(seconds=end-start)
            data = returnvalue.seconds
            break

        with open('save.json', 'r+') as savefile:
            save_data = json.load(savefile)
            temp_data = save_data['projects'][projectname]['total_elapsed_time']
            temp_data += data
            save_data['projects'][projectname]['total_elapsed_time'] = temp_data
            savefile.seek(0)
            json.dump(save_data, savefile, indent=4)
            savefile.truncate()

        try:
            print("You spent {} seconds on {}".format(data, projectname))
        except NameError:
            print('NameError!')
    else:
        return


def load_project():
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)

    # n = 0
    # list_of_projects = []
    # for k in save_data['projects'].keys():
    #     n += 1
    #     print(str(n) + '. ' + k)
    #     list_of_projects.append(k)
    #
    # print('Select which project to load by number: ')
    # load_choice = int(input()) - 1
    chosen_project = list_projects()
    try:
        if chosen_project:
            print('You selected ' + chosen_project +'\nDescription: ' +save_data['projects'][chosen_project]['description'])
            total_elapsed_time = save_data['projects'][chosen_project]['total_elapsed_time']
            print('Total time: '+str(datetime.timedelta(seconds=total_elapsed_time)))
    except IndexError:
        print('Your choice was not in the list')

    print('\n')
    timer(chosen_project)

    return chosen_project #list_of_projects[load_choice]



def list_projects():
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)

        n = 0
        list_of_projects = []
        for k in save_data['projects'].keys():
            n += 1
            print(str(n) + '. ' + k)
            list_of_projects.append(k)

        print('Select project by number: ')
        choice_for_index = int(input()) - 1
        choice_of_project = list_of_projects[choice_for_index]
        return choice_of_project


def edit_projects():
    projectname = list_projects()
    print('1. (D)elete project\n2. (R)eset time of project\n3. (E)dit time manually')
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
        print('Reseting elapsed time in ' + str(projectname) +'...')
        save_data['projects'][projectname]['total_elapsed_time'] = 0
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
        pass



def delete_project(projectname):
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        print('Deleting ' + str(projectname) + '...')
        del save_data['projects'][projectname]
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
        pass


def edit_time(projectname):
    with open('save.json', 'r+') as savefile:
        save_data = json.load(savefile)
        print('Enter the amount of time you want to add or subtract')
        minutes = int(input('Minutes::'))*60
        hours = int(input('Hours:: '))*3600
        new_data = minutes + hours
        temp_data = save_data['projects'][projectname]['total_elapsed_time']
        temp_data += new_data
        save_data['projects'][projectname]['total_elapsed_time'] = temp_data
        savefile.seek(0)
        json.dump(save_data, savefile, indent=4)
        savefile.truncate()
