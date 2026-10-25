# read inputs from config file

import configparser as config
from loguru import logger


config_n = config.ConfigParser()

config_n.read(r"E:\python_projects\config\config_file.ini")

cost_of_brick = config_n["raw_materials"]["cost_of_brick"]
logger.info(cost_of_brick)

