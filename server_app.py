import mongobd_oparations as db

global socket
global c_address

# Utility functions
def recive_from_client():
    message = socket.recv(1024).decode('utf-8')
    
    print(f"{c_address} Message \"{message}\" recived")
    
    return message

def send_to_client(message):
    print(f'{c_address} Message \"{message}\" sent')
    
    socket.send(message.encode('utf-8'))

# APP
def app(client_socket, client_address):
    global socket
    global c_address
    socket = client_socket
    c_address = client_address
    
    logging_menu()


def logging_menu():
    userInput = 0
    
    while (userInput != 3):
        userInput = int(input("Welcome to Coucou! Choose the option: \n1.Register\n2.Log In\n3.Exit"))
        
        if userInput == 1:
            register_menu()
        elif userInput == 2:
            login_menu() 

def register_menu():
    pass

def login_menu():
    pass