#!/usr/bin/python
print('Content-type: text/html\n\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'fuelwatch.db'
connection = sqlite3.connect(mydb)
cursor = connection.cursor()

print('<p><a href="../index.html">Return to Home Page</a></p>')
###############################
# SET UP DATABASE
#
# Drop the tables from the database if they exist so we can run the CREATE statements
# NOTE: If there is data in the database, tables need to be dropped in the correct order 
# to maintain referential integrity
#
print('Drop tables if they exist<br />')
query = """
        DROP TABLE IF EXISTS Price;
        DROP TABLE IF EXISTS Station;
        DROP TABLE IF EXISTS Area;
        DROP TABLE IF EXISTS Product;
        DROP TABLE IF EXISTS Region;
        DROP TABLE IF EXISTS Brand;
        """
# Use executescript as there are multiple queries in the same string
cursor.executescript(query)

# Update the database to allow foreign keys to enforce referential integrity
print("Update PRAGMA to support foreign keys<br />")
query = "PRAGMA foreign_keys = ON"
cursor.execute(query)

###############################
# CREATE EMPTY TABLES
#
# Create each individual table in the database.
# NOTE: Tables need to be created in correct order to ensure foreign key constraints will work
#
print("Create Region Table<br />")
query = """CREATE TABLE Region (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )"""
cursor.execute(query)

print("Create Area Table<br />")
query = """CREATE TABLE Area (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    region_id INTEGER NOT NULL,
    FOREIGN KEY(region_id) REFERENCES Region(region_id)
    )"""
cursor.execute(query)

print("Create Brand Table<br />")
query = """CREATE TABLE Brand (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )"""
cursor.execute(query)

print("Create Product Table<br />")
query = """CREATE TABLE Product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    description TEXT NOT NULL
    )"""
cursor.execute(query)

print("Create Station Table<br />")
query = """CREATE TABLE Station (
    station_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    postcode TEXT,
    brand_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    FOREIGN KEY(brand_id) REFERENCES Brand(brand_id),
    FOREIGN KEY(area_id) REFERENCES Area(area_id)
    )"""
cursor.execute(query)

print("Create Price Table<br />")
query = """CREATE TABLE Price (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    price INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    station_id INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Product(product_id),
    FOREIGN KEY(station_id) REFERENCES Station(station_id)
    )"""
cursor.execute(query)

###############################
# COMMIT CHANGES
#
# Commit changes to the database so they are saved to the database and close connection.
# Any changes that are made prior to a commit will not be saved until they are committed.
#
connection.commit()
connection.close()