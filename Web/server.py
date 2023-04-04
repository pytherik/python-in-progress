from http.server import HTTPServer, BaseHTTPRequestHandler
from config import HOST, PORT


class NeuralHTTP(BaseHTTPRequestHandler):

    content = "HALLOOOO WEELLLTTTT"
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(f'<html><body><h1>{self.content}</h1></body></html>', 'utf-8'))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server läuft jeztz...")

server.serve_forever()
