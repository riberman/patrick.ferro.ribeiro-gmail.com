# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import socket

PORT_NUMBER = 80

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("""<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Patrick Ribeiro Server</title>

        <meta name="author" content="Patrick Ferro Ribeiro">
        <meta name="description" content="Site em construção">

	<link rel="shortcut icon" href="https://riberman.github.io/static/img/favicon.ico">

	<style>
	      body {
		padding-bottom: 40px;
	      }

	      .container-narrow {
		margin: 0 auto;
		max-width: 600px;
		margin-top: 20px;
	      }
	      .container-narrow > hr {
		margin: 30px 0;
	      }

	      .marketing {
		margin: 20px 0;
	      }
	      .marketing p + h4 {
		margin-top: 28px;
		text-align: justify
	      }
	     .justify{
		text-align: justify
	      }
	</style>
</head>

<body>
    <div class="container-narrow">

	<img alt="Logotipo do IFSC" src="https://riberman.github.io/static/img/avatar.png" height="75px" width="75px" />
	<hr>
        <h4 class="marketing"><p>Prezado visitante,</p></h4>
	<p class="text-left marketing justify">O site se encontra em manutenção.<br>
	<p class="text-right"><b>Atenciosamente,</b><br>
	Patrick Ferro Ribeiro</p>
        <hr>
      <hr>
      <div class="footer text-center">
        <p>© Patrick Ferro Ribeiro 2020</p>
      </div>
    </div>
</body>
</html>""")
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
