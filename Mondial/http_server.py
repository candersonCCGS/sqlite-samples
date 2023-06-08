#! /usr/bin/env python3

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# https://docs.python.org/3/library/http.server.html

import http.server
import webbrowser

PORT = 8000

script_path = "index.html"

server_class = http.server.HTTPServer
handler_class = http.server.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

url = f'http://localhost:{PORT}/{script_path}'

webbrowser.open_new_tab(url)

print("serving at", url)

httpd.serve_forever()