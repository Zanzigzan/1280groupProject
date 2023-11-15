global socket

def get_message():
    return socket.recv(1024).decode('utf-8')

def send_message(message):
    socket.send(message.encode('utf-8'))

def app(client_socket):
    global socket
    socket = client_socket
    
    while True:
        message = get_message()
        send_message(message)