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