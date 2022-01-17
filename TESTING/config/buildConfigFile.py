import configparser

config = configparser.ConfigParser()

config.add_section('user')
config.set('user', 'admin', 'Jonatan')

with open('config.ini', 'w') as configfile:
    config.write(configfile)
