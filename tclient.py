global user_name
global socket

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')
    
    return message

def send_to_server(message):
    socket.send(message.encode('utf-8'))

def register():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirmPassword = input("Confirm your password: ")
        if(password == confirmPassword):
            send_to_server(username)
            send_to_server(password)
            recive_from_server()
            break
        else:
            print("Please reconfirm your password.")
            
def login():
    pass

def exit():
    pass

def Menu():
    while True:
        userInput = input("Welcome to Coucou! Choose the option: \n1.Register\n2.Log In\n3.Exit\n")
        if (userInput== "1"):
            send_to_server("1")
            register()
            break
        elif (userInput== "2"):
            send_to_server("2")
            login()
            break
        elif (userInput== "3"):
            send_to_server("3")
            exit()
            break
        else:
            print("Wrong number. Please input the correct number.")
        
    
### APP
def app(client_socket):
    global socket
    global user_name
    socket = client_socket

    
    while True:
        Menu()