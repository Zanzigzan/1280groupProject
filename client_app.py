import ast
global username
global password
global socket
global friendname

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')

    return message

def send_to_server(message):
    socket.send(message.encode('utf-8'))

#######################################################

# it throws an error, we can't send the input successfully
def send_message():
    userInput = input("Type your message: ")
    print(userInput)
    send_to_server(userInput)

# we assume to send the index of the message to server, need to double check
def delete_message():
    get_messages()
    userInput = input("Choose the message to delete: ")
    send_to_server(userInput)

def get_messages():
    messages = recive_from_server()
    msg_array = ast.literal_eval(messages)
    for count, msg in msg_array:
        print(f'{count}. {msg}')

def report_user():
    print("Do you want to report this user: ", friendname)
    userInput = input("1.Yes\n 2.No\n")
    send_to_server(userInput)


def open_chat():
    # is this the correct way to add a global variable
    global friendname
    friendname = recive_from_server()
  
    get_messages()

    while True:
        userInput = input("Choose the option: \n1.Send a message\n2.Delete a message\n3.Refresh\n4.Report the user\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (userInput== "1"):
            send_to_server(userInput)
            send_message()
        elif (userInput== "2"):
            send_to_server(userInput)
            delete_message()
        elif (userInput== "3"):
            send_to_server(userInput)
            get_messages()
        elif (userInput== "4"):
            send_to_server(userInput)
            report_user()
        else:
            print("Wrong input. Please input the correct number.")



def open_userlist():
    while True:
        print("Choose a user:")

        users = recive_from_server()

        users_array = ast.literal_eval(users)
        for count, name_pair in enumerate(users_array):
            for name in name_pair:
                if name != username:
                    print(f"{count}. {name}")
        
        userInput = input("Exit\n") 

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (int(userInput) < len(users)):
            send_to_server(userInput)
            open_chat()
        else:
            print("Wrong input. Please input the correct number.")

def change_username():
    userInput = input("New username: ")
    print(f'Do you want to change your username to  {userInput}?')
    userconfirm = input("1.Yes\n2.No\n")
    if(userconfirm == "1"):
        send_to_server("yes")
        send_to_server(userInput)
    else:
        send_to_server("no")
    
   
def change_password():
    userInput1 = input("New password: ")
    userInput2 = input("Confirm your new password: ")
    if(userInput1 == userInput2):
        send_to_server("yes")
        send_to_server(userInput1)    
    else: 
        print("Password doesn't match")
        send_to_server("no")
        

def user_menu():
    while True:
        userInput = input("Choose the option: \n1.Open chats\n2.Change your username\n3.Change your password\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (userInput== "1"):
            send_to_server(userInput)
            open_userlist()
        elif(userInput== "2"):
            send_to_server(userInput)
            change_username()
        elif(userInput== "3"):
            send_to_server(userInput)
            change_password()
        else:
            print("Wrong input. Please input the correct number.")

def login():
        #add username to be global, to be used in open_listusers()
        global username
        global password
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        send_to_server(username)
        send_to_server(password)   
        msg = recive_from_server()
        print(msg)
        if(msg == "Logged in"):
            user_menu()
    


def register():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirmPassword = input("Confirm your password: ")
        if(password == confirmPassword):
            send_to_server(username)
            send_to_server(password)
            msg = recive_from_server()
            print(msg)
            if(msg == "User created successfully"):
                break
        else:
            print("Please reconfirm your password.")


def Menu():
    while True:
        userInput = input("Welcome to Coucou! Choose the option: \n1.Register\n2.Log In\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        if (userInput== "1"):
            send_to_server(userInput)
            register()
        elif (userInput== "2"):
            send_to_server(userInput)
            login()
        else:
            print("Wrong input. Please input the correct number.")
        
    
### APP
def app(client_socket):
    global socket
    socket = client_socket

    Menu()