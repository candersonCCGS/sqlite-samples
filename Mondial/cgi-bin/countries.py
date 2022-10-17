#!/usr/bin/python
print('Content-type: text/html\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

from DB_Functions import *

mydb = 'mondial.db'
conn = sqlite3.connect(mydb)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

#####
# Start building the HTML for the results of your database query
#
# Add the title and the name of the CSS stylesheet as parameters
#
startHTML("Mondial Database", "stylesheet")
#
# Add a heading to your results page
#
print('<h1>Countries of the World</h1>')
print('<p>The following table lists the countries</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute
#
cursor.execute('''SELECT * FROM Country''')
records = cursor.fetchall()
#
#####

#####
#
# Build the rest of the HTML to show your results.
#
# Build the HTML table with the results from the database query
print_Records(records)
#
# Add the end of the HTML
endHTML()

conn.close()
