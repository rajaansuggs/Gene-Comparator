#!/usr/bin/env python3
import pymysql    # MySQLdb
import cgi, cgitb

cgitb.enable();

# Create instance of FieldStorage 
form = cgi.FieldStorage()
seqname = form.getvalue('geneName')


db = pymysql.connect(host="localhost",  # your host 
                     user="suggsrc",       # username
                     passwd="bio466",     # password
                     db="suggsrc")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM Gene82  WHERE geneName= \"" + seqname + "\"")

# Start webpage
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Form Results</title>")
print ("</head>")
print ("<body>")

# print the first, second, and third columns to a table
results = cur.fetchall()

if len(results) > 0:
        print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Chromosome</th><th>Gene Id</th><th>Start</th><th>End</th><th>Gene Name</th><th>Transcript ID</th><th>Version</th> </tr>")
        for row in results:
            print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2]) + "</td><td>"+ str(row[3]) +"</td><td>"+ str(row[4])+ "</td><td>"+ str(row[5])+ "</td><td>"+ str(row[6])+ "</td> </tr>")

        print ("</table>")
else:
        print ("<p><i>No matches found</i></p>")

db.close()

print ("</body>")
print ("</html>")
