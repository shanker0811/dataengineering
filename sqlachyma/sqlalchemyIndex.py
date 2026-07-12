from . import logger
import os
from sqlalchemy import create_engine
from sqlalchemy import text
db_url=os.getenv('DATA_BASE_URL')
print(db_url)
sqlengine=create_engine(db_url)
logger.info("connection to db using sqlalchyma initiated")
try:
    with sqlengine.connect() as coonection:
        logger.info("connection to db using sqlalchyma sucessfull")
        rows=coonection.execute(text('Select * from employees'))
        _rows=rows.fetchone()
        employees=_rows._mapping['emp_name']
        print(employees,"15................")

except Exception as e :
    logger.warning('Connection failed',e)
