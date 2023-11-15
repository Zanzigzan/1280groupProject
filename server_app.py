def app(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        
        if message:
            client_socket.send(message.encode('utf-8'))