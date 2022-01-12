import configparser

config = configparser.ConfigParser()
config.read('config.ini')
userInfo = config["user"]
admin = userInfo["admin"]
print(admin)
