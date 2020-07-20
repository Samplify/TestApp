import pycurl
import logging
import time
import os
import sys
import concurrent.futures
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Pulls variable from host env variable, validates executions per second is between 0 and 30 and if not, sets it to 10
try:
    if (os.environ['EXECUTIONS_PER_SECOND'] <= 0) or (os.environ['EXECUTIONS_PER_SECOND'] > 30):
        executions_per_second = 10
    else:
        executions_per_second = os.environ['EXECUTIONS_PER_SECOND']
except:
    executions_per_second = 10

#set URL to docker container env variable TEST_URL
try:
    url = os.environ['TEST_URL']
except:
    #Close if no url is found
    sys.exit()

#set up logger
log_path = "log/testerapp.log"
logger = logging.getLogger("rotating_log")
logging.basicConfig(
        handlers=[RotatingFileHandler(log_path, maxBytes=2000000, backupCount=10)],
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s")

#set up curl object
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.FOLLOWLOCATION, True)

#perform curl and log

def tester():
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                log_entry = None #blank log entry variable
                c.perform() #perform curl, return success log + TTLB
                log_entry = ('status=success ' + 'TTLB=%f ' % c.getinfo(c.TOTAL_TIME)) # set log variable to success + TTLB
                logging.info(log_entry) #add the log entry
                time.sleep(1 / executions_per_second)

        except:
            logging.warning('status=fail ' + 'TTLB=%f ' % c.getinfo(c.TOTAL_TIME))
            time.sleep(1 / executions_per_second)

if __name__ == "__main__":
    tester()