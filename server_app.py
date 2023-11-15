global socket
global userInput
global exitButton

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



def firstMenu():
    userInput = int(input("Welcome to Coucou! Choose the option: \n1.Register\n2.Log In\n3.Exit"))
    if userInput == 1:
        register()
    elif userInput == 2:
        LogIn()
    elif userInput == 3:
        