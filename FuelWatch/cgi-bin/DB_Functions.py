# Build HTML table to disaply all records that have been found
def print_Records(records):
	if len(records) > 0:
		print('<table>')
		# Build header row using key values of fields that have been returned
		print('<thead>')
		print('    <tr>')
		for field in records[0].keys():
			print('        <th>' + str(field) + '</th>')
		print('    </tr>')
		print('</thead>')

		# Build table row for each record that has been returned.
		print('<tbody>')
		for record in records:
			print('    <tr>')
			for field in record:
				print('        <td>' + str(field) + '</td>')
			print('    </tr>')
		print('</tbody>')
		print('</table>')
	else:
		# Return paragraph if not records have been found
		print('<p class="no_records">No records found</p>')

# Build the start of the html page, including title and link to stylesheet
def startHTML(title, stylesheet):
	print(f'''<!DOCTYPE html>
<html>
<head>
	<title>{title}</title>
	<link rel="stylesheet" href="../{stylesheet}.css">
</head>
<body>''')
	createHeader()

# Build end of html page
def endHTML():
	createFooter()
	print('''</body>
</html>''')

def createHeader():
	print('<header>')
	print('    <p><a href="../index.html">Return to Home Page</a></p>')
	print('</header>')

def createFooter():
	print('<footer>')
	print('    <p><a href="../index.html">Return to Home Page</a></p>')
	print('</footer>')
