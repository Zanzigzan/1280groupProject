def app(client_socket):
    while True:
        message = input("Message: ")
        
        if message:
            client_socket.send(message.encode('utf-8'))
            message = client_socket.recv(1024).decode('utf-8')
            print(message)