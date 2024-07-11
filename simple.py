import time
import os
import sys
from colorama import Fore, Back
import linecache

#letter colors | or just colors
black = Fore.BLACK
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
white = Fore.WHITE
cyan = Fore.CYAN
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
reset_color = Fore.RESET

#Background colors
background_yellow = Back.YELLOW
background_magenta = Back.MAGENTA
background_cyan = Back.CYAN
background_red = Back.RED
background_white = Back.WHITE
background_green = Back.GREEN
background_black = Back.BLACK
background_blue = Back.BLUE
background_reset = Back.RESET

def wait(timetowait):
    time.sleep(timetowait)

def say(message):
    print(message)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit():
    sys.exit()

def quit():
    sys.exit()

def prompt(toask):
    return input(toask)

def ask(toask):
    return input(toask)

def create_file(filename):
    with open(filename, 'w'):
        pass

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def readline(filename, line):
    return linecache.getline(filename, line)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(red + f"{filename} does not exist." + reset_color)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        print(red + f"{folder} exist already." + reset_color)

def delete_folder(folder):
    if os.path.exists(folder):
        os.rmdir(folder)
    else:
        print(red + f"{folder} does not exist." + reset_color)

def file_exists(filename):
    return os.path.exists(filename)

def current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def pause(texttopause):
    input(texttopause)

def change_directory(path):
    os.chdir(path)
