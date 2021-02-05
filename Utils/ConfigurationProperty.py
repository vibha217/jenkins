from jproperties import Properties

#Creating Properties object and loading file in it
configs = Properties()
with open('', 'rb') as config_file:
    configs.load(config_file)