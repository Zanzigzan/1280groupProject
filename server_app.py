import mongobd_oparations as db

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
    
#############################################

def send_message():
    msg = recive_from_client()
    print(msg)
    db.insert_message(username, friendname, msg)


def delete_message():
    userInput = recive_from_client()
    db.delete_message(username, friendname,int(userInput))

def get_messages():
    messages = db.get_messages(username,friendname)
    send_to_client(str(messages))

def report_user():
    userInput = recive_from_client()
    if(userInput == "1"):
        db.report_user(friendname, username)


def open_chat():
    send_to_client(friendname)
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
        elif (userInput== "4"):
            report_user()


def open_userlist():
    while True:
        users = db.get_chats(username)

        #print(users) #TEST
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
    db.create_chat(userInput)


def update_username():
    userInput = recive_from_client()
    if(userInput == "yes"):
        newUsername = recive_from_client()
        # call the change_username func in db
   
def update_password():
    print("a")

    userInput = recive_from_client()
    if(userInput == "yes"):
        print("b")
        userName = recive_from_client()
        print("x")
        newPassword = recive_from_client()
        print("x")
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
            update_username()
        elif (userInput == "3"):
            update_password()

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