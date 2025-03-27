from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        # Chama o script para iniciar o runner
        subprocess.run(["/home/nsee/start_runner.sh"])

# Configurar o servidor
server_address = ('127.0.0.1', 8000)  # Porta 8000
httpd = HTTPServer(server_address, WebhookHandler)

print("Servidor Webhook rodando na porta 8000...")
httpd.serve_forever()
