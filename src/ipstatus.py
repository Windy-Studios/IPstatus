from requests import get
from time import time 
from datetime import datetime
from os import path
import sys as sys
from json import loads, dumps

silent_mode = True if (sys.argv[1] == 1) else False
curr_dir = __file__
data_dir = curr_dir + '../user_data/ipstatus_config.cfg'
if silent_mode:
    define_config()

#------------------------------------------------------------------------------------------------------------
#Program Loop
#------------------------------------------------------------------------------------------------------------
while True:
    curr_sec = datetime.fromtimestamp(time()).second

    while curr_sec < 2:
        current_config = read_config()
        current_ip = get('https://api.ipify.org').content.decode('utf8')
    
        if current_ip != current_config['IP']:
            current_config['IP'] = current_ip
            write_config(data_dir)
            send_status_email()

    while ( curr_sec > 2 ) and ( not silent_mode ):
        user_in = input()
        user_commands(user_in)


#------------------------------------------------------------------------------------------------------------
# Configuration Modification
#------------------------------------------------------------------------------------------------------------

def write_config(config_dict):
        jsn = dumps(config_dict)
        with open(data_dir) as f:
            f.write(jsn)
    return None

def read_config()
    with open(data_dir) as f:
        configuration_text = f.read()
    return loads(configuration_text)


def define_config():
    if path.isfile(data_dir):
        response = input('Configuration exists. Modify y/n')
        if response == 'y':
            modify = True
        elif response == 'n':
            modify = False
        else:
            print('Choose a valid response.')
            define_config()
    else:
        modify = True

    if modify:
        MACHINE_NAME = input('Enter the machine name for this configuration: ')
        EMAIL_SERVER = input('Enter the email sever (gmail: smtp.gmail.com): ')
        EMAIL_PORT = input('Enter the email port (gmail: 587): ')
        PASSWORD = input('Enter your email password: ')
        EMAIL = input('Enter the email address to update to: ')
        IP = input('Enter the current ip or a dummy ip: ')
        STRING = input('Enter an email identifier string: ')
        
        config_dict = {'SERVER_NAME': SERVER_NAME,
                       'EMAIL': EMAIL,
                       'IP': IP,
                       'STRING': STRING}
        write_config()
    return None

def send_status_email(config):



#------------------------------------------------------------------------------------------------------------
# User Inputs 
#------------------------------------------------------------------------------------------------------------
def user_commands(user_input):
    if user_input == 'x':
        exit()
    
    elif user_input = 'r':
        define_config()

    elif user_input = 'e':
        send_status_email()

    elif user_input = 's':
        print('Current IP: ' + current_ip)
        print('Email address: ' + config['email'])

    elif user_input = 'h':
        print('x to exit, r to redefine configuration, e to send configuration email, s to print current status.')

    else:
        print('h for help')
#------------------------------------------------------------------------------------------------------------
# Cryptography 
#------------------------------------------------------------------------------------------------------------

def grab_key():
    key_dir = curr_dir + 'key.txt'
    if os.isfile(key_dir):
        with open(key_dir, 'rb') as filekey:
            key = filekey.read()
    else:

