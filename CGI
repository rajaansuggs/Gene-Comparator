
#!/File Name: cgi.db.1.py
#!/usr/bin/python3.7
import pymysql, cgi, cgitb
cgitb.enable()
db = pymysql.connect(host="localhost", user="suggsrc", passwd="bio466", db="suggsrc")
# Create a Cursor object to execute queries.
cur = db.cursor()
cur.execute("SELECT * FROM Gene.98 FROM Gene WHERE geneName=\""+geneName+"\"")
 #  Select data from table using SQL query.
print ("Content-type:text/html\r\n\r\n") # Start webpage
print ("<html>")
print ("<head>")
print ("<title>Form Results</title>")
print ("</head>")
print ("<body>")

# print the columns to a table   
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>chromosome</th><th>gg
ene_id</th><th>Start</th></tr>End</th></tr> GeneName</th></tr>transcript_id</th>>
</tr>version</th></tr>transcript_number</th></tr>")
results = cur.fetchall()
if len(results) > 0:
        for row in results:
                print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "<</td><td>"  + str(row[2]) + "</td></tr>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5]) + "</td><td>"+ str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8]) + "</td><td>")
        print ("</table>")
else:
        print ("<p><i>No matches found</i></p>")
cur.close()
del cur
db.close()
print ("</body>")
print ("</html>")
