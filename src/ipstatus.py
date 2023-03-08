from requests import get
from datetime import datetime

dummy_ip = '1.1.1.1'
current_ip = '1.1.1.1'
working_ip = '1.1.1.1'

config = # read file

while True:
    current_ip = get('https://api.ipify.org').content.decode('utf8')

    if current_ip 



def define_config():
    


def user_commands(user_input):
    if user_input == 'x':
        exit()
    
    if user_input = 'r':
        define_config()

    if user_input = 's':
        print('Current IP: ' + current_ip)
        print('Email address: ' + config['email'])


