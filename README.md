# EX01 Developing a Simple Webserver
## Date: 18/05/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
    <head>
        <title>
            TCL/IP Protocol Suite
        </title>
    </head>
    <body>
<h2>List of protocols in TCP/IP Protocol Suite</h2>
        <ol>
            <li>Application Layer:</li>
            <ul>
                <li>Hypertext Transfer Protocol (HTTP/HTTPS)</li>
                <li>File Transfer Protocol (FTP)</li>
                <li>Simple Mail Transfer Protocol (SMTP)</li>
                <li>Domain Name System (DNS)</li>
                <li>Post Office Protocol (POP)</li>
                <li>Internet Message Access Protocol (IMAP)</li>
                <li>Telnet</li>
                <li>Secure Shell (SSH)</li>
                <li>Simple Network Management Protocol (SNMP)</li>
            </ul>
            <li>Transport Layer:</li>
            <ul>
                <li>Transmission Control Protocol (TCP)</li>
                <li>User Datagram Protocol (UDP)</li>
            </ul>
            <li>Internet Layer:</li>
            <ul>
                <li>Internet Protocol (IP) (IPv4 and IPv6)</li>
                <li>Address Resolution Protocol (ARP)</li>
                <li>Reverse Address Resolution Protocol (RARP)</li>
                <li>Internet Control Message Protocol (ICMP)</li>
                <li>Internet Group Management Protocol (IGMP)</li>
            </ul>
            <li>Network Access Layer (or Link Layer):</li>
            <ul>
                <li>Ethernet</li>
                <li>Point-to-Point Protocol (PPP)</li>
                <li>Frame Relay</li>
                <li>ATM (Asynchronous Transfer Mode)</li>
            </ul>
        </ol>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot (351).png>)
![alt text](<Screenshot (352).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
