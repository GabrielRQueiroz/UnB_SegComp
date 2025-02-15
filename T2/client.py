import socket
import ssl

ca_cert_file = 'certificado.pem'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=ca_cert_file)
context.check_hostname = False

with context.wrap_socket(client_socket, server_hostname='localhost') as tls_socket:
    tls_socket.connect(('localhost', 8443))
    print("Conexão segura estabelecida com o servidor.")
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    tls_socket.sendall(request.encode('utf-8'))
    response = tls_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")
