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

    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd='',
        database = 'group4_assignment2'
    )
    
    if username == 'admin':
        # Collect the information of admin user
        mycursor = mydb.cursor(buffered=True)
        query = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
        values = (username,password)
        mycursor.execute(query,values)
        result = mycursor.fetchall()
        
        # Check the password for admin
        if (len(result) == 0):
            mycursor.execute("SELECT * FROM `login` WHERE `username`= '" + username + "'")
            result = mycursor.fetchall()
            if(len(result) > 0):
                print(username + ' is found but wrong password !!!')
                print('<br/>')
                print('<br/>')
                print('<a href="login.html"><button type="button">Back to Login page</button></a>')
            else:
                    print('<h1 class="ui header">Account not found, go back to register you account !!!</h1>')
                    print('<br/>')
                    print('<br/>')
                    print('<a href="register.html"><button type="button">Go to Register page</button></a>')
        # Display the table of all users, admin allows or rejects claim 
        else:
                mycursor.execute("SELECT * FROM `device`")
                result = mycursor.fetchall()
                keys = ['username', 'product_name', 'serial_no', 'purchase_date', 'claim_status', 'comment']
                
                print('<!DOCTYPE html>')
                print('<head>')
                print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"/>')
                print('</head>')
                print('<body>')
                print('<form id="claim_form" action="admin.py" method="POST">')
                print('<fieldset>')
                print('<h2>ADMIN APPROVE OR REJECT CLAIM</h2>')
                print('<p><input placeholder="Enter serial number" type="text" name="serial_no" /></p>')
                print('<p><input placeholder="Enter username" type="text" name="username" /></p>')
                print('<p><input placeholder="Update claim status" type="text" name="claim_status" /></p>')
                print('<div><textarea rows="10" cols="50" placeholder="Enter comment ..." name="comment"></textarea></div>')
                print('<button class="ui primary button" type="submit">Modify</button>')
                print('<input class="ui button" type="reset" value="Reset form"/>')
                print('</fieldset>')
                print(' </form>')
                print('<br/>')
                print('<br/>')
                print('<table border="">')
                print('<tr>')
                for i in keys:
                    print('<th>{}</th>'.format(i))
                print('</tr>')
                
                for i in result:
                    print('<tr>')
                    for j in i:
                        print('<td>{}</td>'.format(j))
                    print('</tr>')
                print('</table>')
                print('</body>')
                print('<br/>')
                print('<a href="login.html"><button class="ui inverted secondary button" type="button">Back to Login page</button></a>')
                print('</html>')
    
    # Normal user login to add the product   
    else:
        mycursor=mydb.cursor(buffered=True)
        # Check the infomation of normal user.
        query = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
        values = (username,password)
        mycursor.execute(query,values)
        result = mycursor.fetchall()
        if (len(result) == 0):
            mycursor.execute("SELECT * FROM `login` WHERE `username`= '" + username + "'")
            result = mycursor.fetchall()
            if(len(result) > 0):
                print(username + ' is found but wrong password !!!')
                print('<br/>')
                print('<br/>')
                print('<a href="login.html"><button type="button">Back to Login page</button></a>')
            else:
                print('<h1 class="ui header">Account not found, go back to register you account !!!</h1>')
                print('<br/>')
                print('<br/>')
                print('<a href="register.html"><button type="button">Go to Register page</button></a>')
        # Adding product when normal user login
        else:
            mycursor.execute("SELECT * FROM `device` WHERE `username`= '" + username + "'")
            result = mycursor.fetchall()
            keys = ['username', 'product_name', 'serial_no', 'purchase_date', 'claim_status', 'comment']
            print('<!DOCTYPE html>')
            print('<head>')
            print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"/>')
            print('</head>')
            print('<body>')
            print('<div class="ui card">')
            print('<div class="content">')
            print('<img class="right floated mini ui image" src="./login.png">')
            print('<div class="header">')
            print("Name: ", username)
            print('<div class="meta">')
            print('<div class="content">')
            print('Allow to add device')
            print('</div>')
            print('</div>')
            print('</div>')
            print('</div>')
            print('</div>')
            print('<form action="device.py" method="POST">')
            print('<fieldset>')
            print('<h2>Choose your product:</h2>')
            print('<p>')
            print('<select class="ui dropdown" name="product_name">')
            print('<option value="iphone">IPHONE</option>')
            print('<option value="camera">CAMERA</option>')        
            print('<option value="monitor">MONITOR</option>')
            print('<option value="keyboard">KEYBOARD</option>')
            print('</select>')   
            print('</p>')
            print('<p>')
            print('<input placeholder="Enter your username" type="text" name="username" />')
            print('</p>')        
            print('<p>')  
            print('<input placeholder="Enter serial number" type="text" name="serial_no" />') 
            print('</p>')
            print('<p>')    
            print('<input placeholder="Enter purchase date" type="text" name="purchase_date" />')        
            print('</p>')    
            print('<input class="ui primary button" type="submit" value="Submit"/>') 
            print('<input class="ui button" type="reset" value="Reset form"/>')
            print('</fieldset>')
            print('</form>')
            print('<br/>')
            print('<a href="login.html"><button class="ui inverted secondary button" type="button">Back to Home page</button></a>')
            print('<br/>')
            print('<br/>')
            print('<a href="claims.html"><button class="ui inverted brown button" type="button">Adding on Claim...</button></a>')
            print('<br/>')
            print('<br/>')
            # Display the table information of user, when they buy the product
            print('<table border="">')
            print('<tr>')
            for i in keys:
                print('<th>{}</th>'.format(i))
            print('</tr>')
            
            for i in result:
                print('<tr>')
                for j in i:
                    print('<td>{}</td>'.format(j))
                print('</tr>')
            print('</table>')
            
            print('</body>')
            print('</html>')
            
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
