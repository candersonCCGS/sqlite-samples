##################################################
#
# This code can be used to build a Python CGI file that will
# insert data into a SQLite database.
# 
# The program reads data from csv files and builds the necessary
# INSERT statements.
# 
# To use this script:
#   1. Create a folder called Raw Data in your cgi-bin folder
#   2. Save the csv files with the data for each table in your database in this folder
#         - one csv file for each table in your database
#         - first row should be the field names
#   3. Save this Python script in your cgi-bin folder
#   3. Update the variables below with the lists of file names and database file etc
#   4. Run the Python script from the cgi-bin folder
#
##################################################

##################################################
# FUNCTIONS:
#
#------------------------------
# Build the INSERT queries for the given table
def createQueries(in_name, out_name, table):
  # open output file to add insert statement to
  with open(out_name, 'a') as file_out:
    file_out.write(f"print('Start inserting data into {table} table<br />')\n")

    # open csv file with raw data for table
    with open(f'Raw Data/{in_name}.csv') as file_in:

      # read first line of csv file to get field names for table
      header = file_in.readline()
      field_names = header.lower().strip().split(',')

      # read in rest of csv file and create list of records  
      records = []
      for line in file_in.readlines():
        record = line.strip().split(',')
        records.append(record)

      # for each record read in, build an INSERT statement and write it to the output file
      for record in records:
        if record[0] != '':
          line = f"cursor.execute('''INSERT INTO {table} ("
          line += ', '.join(field_names)
          # for name in field_names:
          #   line += f'{name}, '
          line += ') VALUES ('
          for field in record:
            # if value is a digit add value, otherwise put quotation marks around string
            if field.isdigit():
              line += f'{field.strip()}, '
            else:
              line += f'"{field.strip()}", '
            out_line = f"{line[:-2]})''')\n" # need to strip last ', ' from each line
          file_out.write(out_line)

    file_out.write(f"print('Finish inserting data into {table} table<br />')\n")

#------------------------------
# This adds the code for the start of the CGI program
def setupCGI(dbName, out_file):
  with open(out_file, 'w') as f_out:
    script = '''#!/usr/bin/python
print('Content-type: text/html\\n\\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3\n\n'''
    script += f"mydb = '{dbName}'\n"
    script += '''connection = sqlite3.connect(mydb)
cursor = connection.cursor()\n\n'''
    homepage = '"../index.html"'
    script += f"print('<p><a href={homepage}>Return to Home Page</a></p>')\n\n"
    f_out.write(script)
  
#------------------------------
# This adds the code for the end of the CGI program
def closeCGI(out_file):
  with open(out_file, "a") as f_out:
    script = 'connection.commit()\nconnection.close()'
    f_out.write(script)

##################################################
#
# CHANGE THE FOLLOWING LINES TO PRODUCE YOUR CGI PROGRAM TO INSERT DATA INTO YOUR DATABASE:
#
# These are the input csv files for your data.
# NOTE:
#   1. all csv files need to be in a folder called Raw Data
#   2. the first line in each csv file should contain the list of name of each field
#   3. data needs to be entered in the correct order to ensure referential integrity
in_files = ["Product", "Region", "Brand", "Area", "Station", "Price"]

# These are the tables that each csv file corresponds to
# NOTE: the order of tables must match the order of the csv files
tables = ["Product", "Region", "Brand", "Area", "Station", "Price"]

# The name of the database
database = "fuelwatch.db"

# The name of the python file that you will create
out_file = "insert_data.py"
#
##################################################

##################################################
#
# This code calls the functions to run the program!
#
setupCGI(database, out_file)
for i in range(len(in_files)):
  createQueries(in_files[i], out_file, tables[i])
closeCGI(out_file)
