import logging
from logging.handlers import RotatingFileHandler
handler=RotatingFileHandler(
    filename="proogram.log",
    maxBytes=1024*5*5,
    backupCount=5
)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)
logger.info("Logger configured")
logger.debug("Degugger log")
logger.warning("warning log")
logger.error("error log")
try:
    raise "Error c=occured"

except Exception as e:
    logger.exception(e)
