#!C:\Program Files\Python39\python.exe

# *****************************************************************************
# * SRT211 – Project2
# * I declare that this assignment is my own work in accordance with Seneca Academic
# * Policy.
# * No part of this assignment has been copied manually or electronically from any other
# * source (including web sites) or distributed to other students.
# *
# * Name: Anh Dung Pham         Student ID: 123 196 180   Date: August 3, 2021
# * Name: Tino Asiimwe          Student ID: 158 117 184   Date: August 3, 2021
# *
# *****************************************************************************

import mysql.connector
import cgi

try:
    print("Content-type: text/html \n\n")

    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    cellphone = form.getvalue('cellphone')
    gmail = form.getvalue('gmail')

    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd='',
        database = 'group4_assignment2'
    )
    
    mycursor=mydb.cursor(buffered=True)
    
    # Add information of the user into the database, when user register the account
    query = "INSERT INTO `login` (`username`,`password`,`cellphone`,`gmail`) VALUES (%s, %s, %s, %s)"
    values = (username,password, cellphone, gmail)
    mycursor.execute(query,values)
    print('Register successfully !!!')
    print('<a href="login.html"><button type="button">Back to Login page</button></a>')
    mydb.commit()
    mydb.close()

except (mysql.connector.IntegrityError, mysql.connector.DataError) as error:
    print('<h1>Username has already exist !!!</h1>')
    print('<a href="register.html"><button type="button">Back to register page</button></a>')
    
except (mysql.connector.ProgrammingError) as error:
    print('Programming Error')
    print(error)

except (mysql.connector.Error) as error:
    print(error)

except:
    print('Last exception !!!')
