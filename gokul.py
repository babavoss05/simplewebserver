from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Top 5 Revenue Company</title>
</head>
<body>
<h1><u>Top 5 Revenue Company</u><h1>
<ul>
<li>Apple</li>
<li>Microsoft</li>
<li>BlackBerry</li>
<li>Samsung</li>
<li>Mi</li>
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
