import pandas as pd
import pyodbc

import platform
def dbconnect():
    try:
        connection=pyodbc.connect(
        "DRIVER={MySQL ODBC 9.7 ANSI Driver};"
        "SERVER=localhost;"
        "DATABASE=de_questions;"
        "uid=shanker;"
        "pwd=shanker@0811"
        )
        print("dbconnection successful")
        return connection
    except pyodbc.InterfaceError as e:
        print("Error connecting to the database:", e)
    
if __name__ == "__pandaspyodbc__":
        connection=dbconnect()
        cursor=connection.cursor()
        _rows=cursor.execute("SELECT * FROM EMPDETAILS")
        # first_row=_rows.fetchone()

        # print(first_row)
        allrecords=_rows.fetchall()
        print(allrecords)
        _columns=[col[0] for col in cursor.description]
        # user_id=int(input("Enter the user id:"))
        # user_name=(input("Enter the user Name:"))
        # user_salary=int(input("Enter the user Salery:"))
        # user_depid=int(input("Enter the department id:"))

        # try:
        #     cursor.execute("INSERT INTO employees values(?,?,?,?)",(user_id,user_name,user_salary,user_depid))
        #     print("Record inserted successfully")
        #     connection.commit()
        # except pyodbc.Error as e:
        #     print("Error inserting record:", e)
        #     connection.rollback()
        # list_to_add=  [(209, "Kiran", 65000.00, 2),
        #     (203, "Anjali", 48000.00, 1),
        #     (204, "Vikram", 72000.00, 2),
        #     (205, "Meena", 53000.00, 3),
        #     (206, "Rakesh", 58000.00, 1),
        #     (207, "Pooja", 61000.00, 2),
            # ("Arjun", 208,69000.00, 3),
            # ("Lakshmi", 209, 75000.00, 1),
            # ("Suresh", 210, 45000.00, 2)
            # ]
        # try:
        #     cursor.executemany("INSERT INTO employees values(?,?,?,?)",list_to_add)
        #     print("Record inserted successfully")
        #     connection.commit()
        # except pyodbc.Error as e:
        #     print("Error inserting record:", e)
        #     connection.rollback()

        # cursor.execute("INSERT INTO employees values(106,'shiva',60000,1)")
        # print(pd.__version__)
        # print(pyodbc.version)
        # print(type(allrecords[0]))
        # rows=pd.read_sql("SELECT * FROM EMPDETAILS", connection)
        # print(_rows.fetchall())


        
        dataframe=pd.read_sql("SELECT * FROM employees", connection,index_col='emp_name')
        print(allrecords[0],dataframe)
        connection.close()
