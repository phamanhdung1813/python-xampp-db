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
    serial_no = form.getvalue('serial_no')
    username = form.getvalue('username')
    claim_status = form.getvalue('claim_status')
    comment = form.getvalue('comment')
    
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd='',
        database = 'group4_assignment2'
    )
    
    mycursor=mydb.cursor(buffered=True)
    # Admin user can modify the claim status of normal user, accept or reject or do anything
    query = "UPDATE `device` SET `claim_status`=%s, `comment`=%s WHERE `serial_no`=%s AND `username`=%s"
    
    values = (claim_status, comment, serial_no, username)
    mycursor.execute(query, values)
    
    print('<h2>Modified successfully !!!</h2>')
    print('<button onclick="goBack()">Go Back</button>')
    print('<script>')
    print('function goBack() { window.history.back(); }')
    print('</script>')
    
    mydb.commit()
    mydb.close()

except (mysql.connector.IntegrityError, mysql.connector.DataError) as error:
    print('DataError or IntegrityError')
    print(error)

except (mysql.connector.ProgrammingError) as error:
    print('Programming Error')
    print(error)

except (mysql.connector.Error) as error:
    print(error)

except:
    print('Last exception !!!')
