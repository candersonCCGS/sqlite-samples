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
print(f'<h1>Areas of Western Austalia</h1>')
print(f'<p>A list of all the areas with petrol stations in Western Australia.</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute
# NOTE: Use the values in the dictionary to build your search
#
cursor.execute('''SELECT Area.name as Area, Region.name as Region 
                    FROM Area, Region
                    WHERE Area.region_id = Region.region_id
                    ORDER BY Area.name
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