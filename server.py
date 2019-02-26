from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        if self.path == '/':
            response_text = 'home route'
        else:
            response_text = 'another route'

        self.wfile.write(f'<html><body><h1>{response_text}</h1></body></html>'.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'<!DOCTYPE html><html><head><title> cowsay </title></head><body><header><nav><ul><li><a href="/cow">cowsay</a></li></ul></nav><header><main>project description</main></body></html>'.encode())

if __name__ == "__main__":
    server_address = ('', 5000)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
