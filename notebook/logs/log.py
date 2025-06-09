from us_visa.logger import logging
from us_visa.exception import USVisaexception
import sys

logging.info("Logging setup complete.")

try:
    a=1/0
except Exception as e:
    logging.error(f"Exception occurred: {e} with sys info: {sys.exc_info()}")
    raise USVisaexception(e, sys)
    
    
