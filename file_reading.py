# we have to read an file if file is empty then reise exception
import datetime
from loguru import logger

def read_log_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("File is empty")
            return content
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

content = read_log_file("file1.txt")    
# logger.info(f"Content of the file: {content}")


try:
    counter =0
    names = []
    for line in content.splitlines():
        # logger.info(f"Line: {line}")
        if counter != 0:
            name = line.split(",")[1]
            names.append(name)
            # logger.info(f"Line: {line}")
            logger.info(type(name))
        counter += 1    
        
    set_names = set(names)
    logger.info(set_names)
    

except Exception as e:
    logger.info(e)    
# print(f"Names: {set_names}")
