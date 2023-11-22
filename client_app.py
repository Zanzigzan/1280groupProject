import ast
global username
global password
global socket

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')

    return message

def send_to_server(message):
    socket.send(message.encode('utf-8'))

#######################################################

def send_message():
    userInput = input("Type your message: ")
    print(userInput)
    send_to_server(userInput)

def delete_message():
    pass

def get_messages():
    messages = recive_from_server()
    print(messages)

def open_chat():
    #display all messages related to the user
    get_messages()
    

    while True:
        userInput = input("Choose the option: \n1.Send a message\n2.Delete a message\n3.Refresh\nEXIT\n")

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
    

def user_menu():
    while True:
        userInput = input("Choose the option: \n1.Open chats\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (userInput== "1"):
            send_to_server(userInput)
            open_userlist()
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