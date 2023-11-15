global user_name
global socket

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')
    
    return message

def send_to_server(message):
    socket.send(message.encode('utf-8'))


def app(client_socket):
    global socket
    global user_name
    socket = client_socket

    
    while True:
        message = input("Message: ")
        
        send_to_server(message)
        
        data = recive_from_server()
        
        print(data)