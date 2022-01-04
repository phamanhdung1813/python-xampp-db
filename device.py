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
    product_name = form.getvalue('product_name')
    serial_no = form.getvalue('serial_no')
    purchase_date = form.getvalue('purchase_date')
    
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd='',
        database = 'group4_assignment2'
    )
    
    mycursor=mydb.cursor(buffered=True)
    query = "INSERT INTO `device` (`username`,`product_name`,`serial_no`,`purchase_date`) VALUES (%s, %s, %s, %s)"
    values = (username, product_name, serial_no, purchase_date )
    mycursor.execute(query,values)
    mydb.commit()
    mydb.close()
    
    print('<h2>Added successfully !!!</h2>')
    print('<button onclick="goBack()">Go Back</button>')
    print('<script>')
    print('function goBack() { window.history.back(); }')
    print('</script>')
    

except (mysql.connector.IntegrityError, mysql.connector.DataError) as error:
    print('<h2>Duplicate serial number, enter your product again !!!</h2>')
    print('<button onclick="goBack()">Go Back</button>')
    print('<script>')
    print('function goBack() { window.history.back(); }')
    print('</script>')
    
except (mysql.connector.ProgrammingError) as error:
    print('Programming Error')
    print(error)

except (mysql.connector.Error) as error:
    print(error)

except:
    print('Last exception !!!')
