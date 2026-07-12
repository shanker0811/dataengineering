import pandas as pd
import pyodbc
from pandapyodbc import dbconnect
connection=dbconnect()
cursor=connection.cursor()
cursor.execute("SELECT * FROM employees")
print(cursor.description)
_rows=cursor.fetchall()
_columns=[col[0] for col in cursor.description]
dataFrame=pd.DataFrame.from_records(_rows,columns=_columns)
print(dataFrame)
connection.close()
