import os
from configparser import ConfigParser

config_path = os.path.join('src','backend_core','backend_helpers','CryoDataBotConfig.ini')
config = ConfigParser()
config.read(config_path)

val = config.getint('downloading_and_preprocessing', 'vof_threashold')
print(val)