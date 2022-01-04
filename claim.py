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
    claim_name = form.getvalue('claim_name')
    serial_no = form.getvalue('serial_no')
    purchase_date = form.getvalue('date')
    comment = form.getvalue('comment')
    
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd='',
        database = 'group4_assignment2'
    )
     
    mycursor=mydb.cursor(buffered=True)
    
    query = "SELECT `purchase_date` FROM `device` WHERE `serial_no`='" + serial_no + "' AND `product_name`='" + claim_name + "'"
    mycursor.execute(query)
    date_claim = mycursor.fetchall()
    result_search = mycursor.rowcount
    expire_date = ''
    
    # Count the date from the purchase_date. The protection plan allows only 2 years equal to (730 days)
    if result_search > 0:
        for i in date_claim:
            for j in i:
                query = "SELECT DATEDIFF(CURRENT_TIMESTAMP, '"+ j +"')"
                mycursor.execute(query)
                expire_date = [item for items in mycursor.fetchall() for item in items]
    # Getting current claim status, if the claim is 1 the claim will not be accepted 
    query = "SELECT `claim_status` FROM `device` WHERE `serial_no`='" + serial_no + "' AND `product_name`='" + claim_name + "' AND `purchase_date`='" + purchase_date + "'"
    mycursor.execute(query)
    
    # Getting current claim status, because it is in format list of tuple [(0,)] 
    # So we need to strip the special character and make it appear as integer value
    claim_status = int(((str(mycursor.fetchall()).strip('[]')).strip('()')).strip(','))
    
    if(claim_status == 0):
        # More than 2 years protectin plan condition
        if(int(expire_date[0]) <= 730):
            # Update claim to 1 if the claim lower than 2 years and match all of the conditions
            query = "UPDATE `device` SET `claim_status` = 1, `comment`='"+ comment +"' WHERE `serial_no`=%s AND `purchase_date`=%s"
            values = (serial_no, purchase_date)
            mycursor.execute(query,values)
        else:
            print('<h1>Cannot Claim: Expire within 2 years of protection<h1/>')
    else:
        print('<h1>ONE TIME CLAIM ONLY<h1/>')
    
    mydb.commit()
    mydb.close()
    
    print('Adding claim !!!')
    print('<button onclick="goBack()">Go Back</button>')
    print('<script>')
    print('function goBack() { window.history.back(); }')
    print('</script>')


except (mysql.connector.IntegrityError, mysql.connector.DataError) as error:
    print('Wrong Serial Number on your product !!!')
    
except (mysql.connector.ProgrammingError) as error:
    print('Programming Error')
    print(error)

except (mysql.connector.Error) as error:
    print(error)

except:
    print('<h1>Wrong Information collected to claim !!!<h1/>')
    print('<button onclick="goBack()">Go Back</button>')
    print('<script>')
    print('function goBack() { window.history.back(); }')
    print('</script>')
    