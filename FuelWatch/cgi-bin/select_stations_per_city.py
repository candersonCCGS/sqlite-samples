#!/usr/bin/python
print('Content-type: text/html\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3
from DB_Functions import *

mydb = 'fuelwatch.db'
connection = sqlite3.connect(mydb)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

#####
# Start building the HTML for the results of your database query
#
# Add the title and the name of the CSS stylesheet as parameters
#
startHTML("FuelWatch Database", "results_style")
#
# Add a heading to your results page
#
print(f'<h1>Stations per City</h1>')
print(f'<p>The following table shows the number of stations in each city, sorted based on the number of stations.</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute
# NOTE: Use the values in the dictionary to build your search
#
cursor.execute('''SELECT city, COUNT(city) as "Number of stations" 
                    FROM Station
                    GROUP BY city
					ORDER BY "Number of stations" DESC
                ''')
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

connection.close()