import http.server, socketserver
PORT = 8000
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Game running at http://localhost:{PORT}")
    httpd.serve_forever()
