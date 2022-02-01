# Credit: Smriti Gupta
# Link: https://cppsecrets.com/users/1357411510911410511610510350484964103109971051084699111109/Python-Logging.php

# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="Logging\\newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

"""
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

def write_log_info(message):
    logger.info(message)


