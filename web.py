from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>

<html>
<head>
    <title>TCP/IP Protocols</title>
</head>
<body>

```
<h1>TCP/IP Protocols</h1>

<h2>1. Application Layer</h2>
<p>The Application Layer provides services for users and applications to communicate over a network.</p>
<ul>
    <li><b>HTTP:</b> Used to access web pages on the Internet.</li>
    <li><b>HTTPS:</b> Provides secure communication between a browser and a website.</li>
    <li><b>FTP:</b> Used to transfer files between computers.</li>
    <li><b>SMTP:</b> Used to send emails.</li>
    <li><b>POP3:</b> Used to download emails from a mail server.</li>
    <li><b>IMAP:</b> Used to access and manage emails on a mail server.</li>
    <li><b>DNS:</b> Converts domain names into IP addresses.</li>
    <li><b>SSH:</b> Provides secure remote access to computers.</li>
</ul>

<h2>2. Transport Layer</h2>
<p>The Transport Layer provides communication between devices and ensures data delivery.</p>
<ul>
    <li><b>TCP:</b> Provides reliable and ordered data transmission.</li>
    <li><b>UDP:</b> Provides faster data transmission without guaranteeing delivery.</li>
</ul>

<h2>3. Internet Layer</h2>
<p>The Internet Layer is responsible for sending data packets from one network to another.</p>
<ul>
    <li><b>IP:</b> Provides addressing and routing of data packets.</li>
    <li><b>ICMP:</b> Used for network error reporting and troubleshooting.</li>
    <li><b>IGMP:</b> Manages multicast group communication.</li>
</ul>

<h2>4. Network Access Layer</h2>
<p>The Network Access Layer handles the transmission of data through physical network connections.</p>
<ul>
    <li><b>Ethernet:</b> Used for wired network communication.</li>
    <li><b>Wi-Fi:</b> Used for wireless network communication.</li>
    <li><b>ARP:</b> Finds the MAC address associated with an IPv4 address on a local network.</li>
</ul>
```

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
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()