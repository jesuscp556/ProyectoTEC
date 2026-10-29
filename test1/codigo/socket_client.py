import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345        # Puerto en el que el servidor está escuchando

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
client_socket.connect((HOST, PORT))

# Enviar datos al servidor
message = 'Hola, servidor'
client_socket.sendall(message.encode())

# Recibir respuesta del servidor
response = client_socket.recv(1024)
print('Respuesta del servidor:', response.decode())

# Cerrar la conexión con el servidor
client_socket.close()
