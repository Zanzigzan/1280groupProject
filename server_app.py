import mongobd_oparations as db

global socket
global c_address
global username
global password

# Utility functions
def recive_from_client():
    message = socket.recv(1024).decode('utf-8')
    
    print(f"{c_address} Message \"{message}\" recived")
    
    return message

def send_to_client(message):
    print(f'{c_address} Message \"{message}\" sent')
    
    socket.send(message.encode('utf-8'))
    

def login():
    global username
    global password
    msg = ""
    while msg != "Logged in":
        username = recive_from_client()
        password = recive_from_client()
        msg = db.login(username, password)
        send_to_client(msg)

    
def register():
    msg = ""
    while msg != "User created successfully":
        #login_menu()
        username = recive_from_client()
        password = recive_from_client()
        msg = db.register(username, password)
        send_to_client(msg)


def send_message():
    pass

def delete_message():
    pass

def get_messages():
    
    messages = db.get_messages(username,)
    send_to_client(str(messages))

def open_chat():
    get_messages()

    while True:
        userInput = recive_from_client()

        if userInput.upper() == 'EXIT':
            break
        if (userInput== "1"):
            send_message()
        elif (userInput== "2"):
            delete_message()
        elif (userInput== "3"):
            get_messages()


def open_userlist():
    while True:
        users = db.get_chats(username)

        send_to_client(str(users))

        userInput = recive_from_client()

        if userInput == 'EXIT':
            break
        
        if (int(userInput) < len(users)):
            open_chat()


def user_menu():
    while True:
        userInput = recive_from_client()

        if userInput.upper() == 'EXIT':
            break
        
        if (userInput== "1"):
            open_list()



    
def Menu():
    while True:
        userInput = recive_from_client()

        if userInput.upper() == 'EXIT':
            break

        if userInput == "1":
            register()
        elif userInput == "2":
            login()

### APP
def app(client_socket, client_address):
    global socket
    global c_address
    socket = client_socket
    c_address = client_address

    Menu()