# EX01 Developing a Simple Webserver
## Date:16/03/2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```python
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>
SoftWare Companies
</title>

</head>
<body bgcolor= "Yellow" align="center">

<table align="center" border="5" cellspacing="6" cellpadding="5">
<caption>Top Five Revenue Generating Software Companies</caption>
<tr>
<th> S.No </th>
<th> Company Name </th>
<th> Revenue </th>
</tr>
<tr>
<td> 1 </td>
<td> Microsoft </td>
<td> $86.8 </td>
</tr>
<tr>
<td> 2 </td>
<td> Oracle </td>
<td> $67.1 </td>
</tr>
<tr>
<td> 3 </td>
<td> SAP </td>
<td> $50.9 </td>
</tr>
<tr>
<td> 4 </td>
<td> Walmart </td>
<td> $49.9</td>
</tr>
<tr>
<td> 5 </td>
<td> Google </td>
<td> $40.9 </td>
</tr>
</table>
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
![alt text](<Screenshot (283).png>)

![alt text](<Screenshot 2024-03-22 134026.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
