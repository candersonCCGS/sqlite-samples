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
# Retrieve the search values from the HTML form
form = cgi.FieldStorage()
values = {}
#
# Add the values from the form to a dictionary
region_text = form.getvalue('region_value')
values["region_name"] = region_text
#
#####

#####
# Start building the HTML for the results of your database query
#
# Add the title and the name of the CSS stylesheet as parameters
#
startHTML("FuelWatch Database", "results_style")
#
# Add a heading to your results page
print(f'<h1>Stations in {values["region_name"]}</h1>')
print(f'<p>The following table shows all the stations in the region {values["region_name"]}.</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute.
# NOTE: Use the values in the dictionary to build your search
#
cursor.execute('''SELECT Station.name, Station.address, Station.city, Area.name
                    FROM Station, Area, Region
                    WHERE Region.region_id = Area.region_id
                      AND Area.area_id = Station.area_id
                      AND Region.name = :region_name
                    ORDER BY Station.name''', values)
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