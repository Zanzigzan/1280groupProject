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
    
    
def register_menu():
    username = get_message()
    password = get_message()
    # mongobd_oparations.register(username, password)
    msg = "You have successfully registered.\nYour username is " + username + ", and your password is " + password + "."
    send_message(msg)
    print(username)
    print(password)

        
        
      
def Login_menu():
    userName = get_message()
    password = get_message()
    
def Exit_menu():
    pass
    
def Menu():
    userInput = get_message()
    if userInput == "1":
        register_menu()
    elif userInput == "2":
        Login_menu()
    elif userInput == "3":
        Exit_menu()

### APP
def app(client_socket, client_address):
    global socket
    global c_address
    socket = client_socket
    c_address = client_address
    
    while True:
        Menu()