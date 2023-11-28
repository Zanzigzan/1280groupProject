# Utility functions
def recive_from_client():
    message = ""
    while True:
        part = socket.recv(1024).decode('utf-8')
        if "\n" in part:
            message += part[:part.index("\n")]
            break
        message += part
    print(f"{c_address} Message \"{message}\" recived")
    return message


def send_to_client(message):
    full_message = message + "\n"  # Adding a newline as a delimiter
    print(f'{c_address} Message \"{full_message}\" sent')
    socket.send(full_message.encode('utf-8'))
    
    
    
    
    
# Utility functions
def recive_from_server():
    message = ""
    while True:
        part = socket.recv(1024).decode('utf-8')
        if "\n" in part:
            message += part[:part.index("\n")]
            break
        message += part
    return message


def send_to_server(message):
    full_message = message + "\n"  # Adding a newline as a delimiter
    socket.send(full_message.encode('utf-8'))