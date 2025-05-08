import socket
import os

def handle_request(conn):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Unknown Author')
    
    response = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8  # ← Вот тут!

<h1>Host Information</h1>
<p>Hostname: {hostname}</p>
<p>IP Address: {ip_address}</p> 
<p>Author: {author}</p>
"""
    conn.sendall(response.encode('utf-8'))

def run_server(port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f'Server started on port {port}')
        while True:
            conn, addr = s.accept()
            handle_request(conn)

if __name__ == '__main__':
    run_server()