global socket
global c_address

# Utility functions
def recive_message():
    message = socket.recv(1024).decode('utf-8')
    
    print(f"{c_address} Message \"{message}\" recived")
    
    return message

def send_message(message):
    print(f'{c_address} Message \"{message}\" sent')
    
    socket.send(message.encode('utf-8'))

# APP
def app(client_socket, client_address):
    global socket
    global c_address
    socket = client_socket
    c_address = client_address
    
    while True:
        message = recive_message()
        
        send_message(message)



def firstMenu():
    userInput = int(input("Welcome to Coucou! Choose the option: \n1.Register\n2.Log In\n3.Exit"))
    if userInput == 1:
        register()
    elif userInput == 2:
        LogIn()
    elif userInput == 3:
