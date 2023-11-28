import mongobd_oparations as db
import time

global socket
global c_address
global username
global password
global friendname

# Utility functions
def recive_from_client():
    message = socket.recv(1024).decode('utf-8')
    
    print(f"{c_address} Message \"{message}\" recived")
    
    return message


def send_to_client(message):
    print(f'{c_address} Message \"{message}\" sent')
    
    socket.send(message.encode('utf-8'))
    
    time.sleep(0.2)
    
#############################################

def send_message():
    msg = recive_from_client()
    print(msg)
    res = db.insert_message(username, friendname, msg)
    send_to_client(res)


def delete_message():
    userInput = recive_from_client()
    
    res = db.delete_message(username, friendname,int(userInput))
    send_to_client(res)

def get_messages():
    messages = db.get_messages(username,friendname)
    return str(messages)

def report_user():
    userToBeReported = recive_from_client()
    
    res = db.report_user(userToBeReported, username)
    send_to_client(res)


def open_chat():
    while True:
        messages = get_messages()

        send_to_client(messages)

        userInput = recive_from_client()

        if userInput.upper() == 'EXIT':
            break

        elif (userInput== "2"):
            send_message()
        elif (userInput== "3"):
            delete_message()


def open_userlist():
    while True:
        users = db.get_chats(username)

        send_to_client(str(users))

        userInput = recive_from_client()

        if userInput.upper() == 'EXIT':
            break
        
        if (int(userInput) < len(users)):
            
            global friendname
            friendname = ""
            name_pair = users[int(userInput)]
            for name in name_pair:
                if name != username:
                    friendname = name
            open_chat()


def create_newchat():
    userInput = recive_from_client()
    
    res = db.create_chat(username,userInput)
    send_to_client(res)


def update_username():
    userInput = recive_from_client()
    if(userInput == "yes"):
        newUsername = recive_from_client()
        oldUsername = recive_from_client()
        # call the change_username func in db
        call = db.update_username(oldUsername, newUsername)
        send_to_client(call)
    else:
        send_to_client("Your username will not be changed")
   
def update_password():
    userInput = recive_from_client()
    if(userInput == "yes"):
        userName = recive_from_client()
        newPassword = recive_from_client()
        # call the change_password func in db
        result = db.update_password(userName, newPassword)
        send_to_client(result)
    

def user_menu():
    while True:
        userInput = recive_from_client()

        if (userInput.upper() == 'EXIT'):
            break
        
        if (userInput == "1"):
            open_userlist()
        elif (userInput == "2"):
            create_newchat()
        elif (userInput == "3"):
            update_username()
        elif (userInput == "4"):
            update_password()
        elif (userInput == "5"):
            report_user()

def login():
    global username
    global password
   
    username = recive_from_client()
    password = recive_from_client()
    msg = db.login(username, password)
    send_to_client(msg)
    if(msg == "Logged in"):
        user_menu()
    
        
    
def register():
    msg = ""
    while msg != "User created successfully":
        #login_menu()
        username = recive_from_client()
        password = recive_from_client()
        msg = db.register(username, password)
        send_to_client(msg)

    
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