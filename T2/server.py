import socket
import ssl

cert_file = 'certificado.pem'
key_file = 'chave_privada.pem'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8443))
server_socket.listen(5)
print("Servidor HTTPS aguardando conexões na porta 8443...")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

with context.wrap_socket(server_socket, server_side=True) as tls_socket:
    while True:
        client_socket, client_address = tls_socket.accept()
        print(f"Conexão estabelecida com {client_address}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Dados recebidos: {data}")
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOlá, cliente HTTPS!"
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()
