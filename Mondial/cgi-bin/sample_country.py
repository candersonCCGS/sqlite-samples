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
# Retrieve the search values from the HTML form
form = cgi.FieldStorage()
#
# Add the values from the form to a dictionary
country = form.getvalue('country')
values = { "country": country }
#
#####

#####
# Start building the HTML for the results of your database query
#
# Add the title and the name of the CSS stylesheet as parameters
#
startHTML("Mondial Database", "stylesheet")
#
# Add a heading to your results page
#
print(f'<h1>Information about {country}</h1>')
print(f'<p>The following table lists some of the basic information about {country}.</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute
# NOTE: Use the values in the dictionary to build your search
#
cursor.execute('''SELECT * FROM Country
                   WHERE name = :country''', values)
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