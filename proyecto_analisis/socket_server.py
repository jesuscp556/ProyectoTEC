import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345        # Puerto en el que el servidor estará escuchando

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al puerto y dirección especificados
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes (máximo 1)
server_socket.listen(1)

print('Servidor escuchando en', HOST, PORT)

# Aceptar la conexión entrante
client_socket, address = server_socket.accept()

print('Conexión desde', address)

while True:
    # Recibir datos del cliente
    data = client_socket.recv(1024)
    if not data:
        break
    print('Mensaje recibido del cliente:', data.decode())

    # Responder al cliente
    response = 'Mensaje recibido correctamente'
    client_socket.sendall(response.encode())

# Cerrar la conexión con el cliente
client_socket.close()
