import logging 
import os 
from datetime import datetime 


# below is the name of the file (file structure which is to be used inside the directory)
'''What happens here?

datetime.now() → gets the current date & time

.strftime(...) → formats the date & time into a string

f"...." → f-string (used to insert values into a string)

".log" → file extension for a log file'''

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"


# below codeline will the current working directory and join logs and log file and cwd
'''What it does:

os.getcwd() → gets current working directory

Example: D:\sensor project


"logs" → folder name

LOG_FILE → the file name'''
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# now creating the directory with the path
''''''
os.makedirs(logs_path, exist_ok = True)


# making final log path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

'''This tells Python how to store logs.

🔹 filename=LOG_FILE_PATH

All logs will be written into this file.

🔹 format= ...

Controls how each log entry looks:

Part	Meaning
%(asctime)s	Time of log
%(lineno)d	Line number
%(name)s	Logger name
%(levelname)s	Log level (INFO, ERROR, etc.)
%(message)s	Actual log message'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    # when the logs will be added in the file it will be in format as given below
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



# use the given code below for more readablity
'''import os
import logging
from datetime import datetime

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs folder path
logs_path = os.path.join(os.getcwd(), "logs")

# Create logs folder if not exists
os.makedirs(logs_path, exist_ok=True)

# Create full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
'''