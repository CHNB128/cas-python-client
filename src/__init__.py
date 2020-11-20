import socket
import json

def get_client(host, port):
    client = (host, port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(client)
        return client

def parse_token(client, token):
    message = { 'action': '/sessions/parse', 'data': { 'token': token }}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(client)
        s.sendall(json.dumps(message).encode())
        data = s.recv(1024).decode()
        return repr(json.loads(data))
