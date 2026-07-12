import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
load_dotenv()

handlers=RotatingFileHandler(
    filename='sqlalchymalogs.log',
    maxBytes=1024*5*5,
    backupCount=6
    
)
print(__name__)
if __name__ == 'sqlachyma':
    logging.basicConfig(
        handlers=[handlers],
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'

    )
    logger=logging.getLogger(__name__)
    

