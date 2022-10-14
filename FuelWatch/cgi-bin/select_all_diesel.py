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
print(f'<h1>Price of Diesel</h1>')
print(f'<p>The price of diesel at all stations listed from cheapest to most expensive.</p>')
#
#####

#####
#
# Build your SQL query here for the program to execute
#
cursor.execute('''SELECT Price.date, Price.price, Brand.name, Station.name, Station.city
                    FROM Product, Price, Station, Brand
                    WHERE Product.product_id = Price.product_id
                      AND Price.station_id = Station.station_id
                      AND Station.brand_id = Brand.brand_id
                      AND Product.code = "Diesel"
                    ORDER BY Price.price ASC
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