from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {"service": "beef1", "status": "healthy", "version": "1.0.0"}
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("beef1 running on port 8080")
    server.serve_forever()
