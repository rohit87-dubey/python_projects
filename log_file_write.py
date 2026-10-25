# write a program in which function takes logs as input 
# from user and writes them to a log file with timestamp.

import datetime
from genericpath import exists
from loguru import logger

def write_logs_to_file(logs):
    # Configure logger to write to a file
    # input log is an dictionary with keys as log level and values as log messages

    # logger.add("user_logs.log", format="{time} {level} {message}", level="INFO", rotation="1 MB")

    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if exists("user_logs.log"):
        logger.info("Log file already exists. Appending logs to the existing file.")

        with open("user_logs.log", "a") as log_file:
            for key, value in logs.items():
                log_file.write(f"{timestamp} - {key}: {value}\n")
    else:
        logger.info("Log file does not exist. Creating a new log file.")

        with open("user_logs.log", "x") as log_file:
            for key, value in logs.items():
                log_file.write(f"{timestamp} - {key}: {value}\n")            




    # Write logs to the log file with timestamp
    # for log in logs:
    #     logger.info(f"{timestamp} - {log}")

    logger.info("Logs have been written to user_logs.log")




def logging(**logging):
    # This function takes logs as input from user and store it into dictionary write into file
    write_logs_to_file(logging)

dict_logs = {"status": "Success", "status_code": 200,"message": "This is a log message", "error": "No error"}

logging(**dict_logs)


dict_logs = {"status": "Failed", "status_code": 500, "message": "This is a log message", "error": "error"}

logging(**dict_logs)




