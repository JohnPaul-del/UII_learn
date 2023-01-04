import os
import sys
import shutil
from pprint import pprint
from time import sleep

OPTIONS = {'mk': 'Create dir',
           'cf': 'Create File',
           'del': 'Delete dir or file',
           'cp': 'copy dir or file',
           'ls': 'Show dirs and files',
           'lf': 'show files only',
           'ld': 'show dirs only',
           'si': 'System info',
           'info': 'About creator',
           'ex': 'Exit from FM',
           }


def create_dir():
    print('+' * 30)
    path_ = input(f'Enter path or dir name for creating: ')
    if os.path.exists(path_):
        print('Already Exists! Try again')
        create_dir()
    else:
        os.mkdir(path_)
        print(f'{path_} Successful created')
        welcome()


def create_file():
    print('+' * 30)
    f_name = input(f'Enter file name: ')
    f_dir = os.getcwd()
    f_path = os.path.join(f_dir, f_name)

    if f_path:
        print(f'Already Exists!')
        create_file()
    else:
        with open(f_name, 'w') as f:
            f.close()
        print(f'{f_name} Successful created')
        welcome()


def remove():
    print('+' * 30)
    f_name = input(f'Enter dir name for deleting: ')
    if not os.path.exists(f_name):
        print('Does not Exists! Try again')
        remove()
    else:
        os.rmdir(f_name)
        print(f'{f_name} Successful deleted')
        welcome()


def copy_df():
    cp_from = input('Enter copy path from: ')
    cp_to = input('Enter path copy to: ')
    shutil.copy(cp_from, cp_to)
    welcome()


def show_ls():
    print('+' * 30)
    print(f'{os.listdir()}')
    welcome()


def show_dirs():
    print('+' * 30)
    print(*(f for f in os.listdir() if not os.path.isfile(f)))
    welcome()


def show_files():
    print('+' * 30)
    print(*(f for f in os.listdir() if os.path.isfile(f)))
    welcome()


def info():
    print(f'++++++ (c), I.Pavlov aka John Poul ++++++'
          f'=========================================')
    welcome()


def sys_info():
    print(f'+++++++++++++++++++++++++++++++++++++++++'
          f'Sys: {os.uname().sysname}\n'
          f'Version: {os.uname().version}'
          f'=========================================')
    welcome()


def welcome():

    print(f'Welcome to FM!\n'
          f'Chose option:')
    for k, v in OPTIONS.items():
        print(f'    {k} - {v}')

    action = input('Enter option: ')

    if action == 'ex':
        quit()
    elif action == 'mk':
        create_dir()
    elif action == 'cf':
        create_file()
    elif action == 'del':
        remove()
    elif action == 'cp':
        copy_df()
    elif action == 'ls':
        show_ls()
    elif action == 'lf':
        show_files()
    elif action == 'ld':
        show_dirs()
    elif action == 'info':
        info()
    elif action == 'si':
        sys_info()
    else:
        sleep(3)
        print('Error! Try again')
        welcome()


welcome()
