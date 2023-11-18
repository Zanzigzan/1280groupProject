import json
global user_name
global socket

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')

    return message

def send_to_server(message):
    socket.send(message.encode('utf-8'))

#######################################################

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



def send_message():
    pass

def delete_message():
    pass

def get_messages():
    pass



def open_chat():
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
        print("Choose the option: \n")

        users = recive_from_server()
        users_array = json.loads(users)
        for count, ele in enumerate(users_array):
            print(f"{count}. {ele}")
        

        userInput = input("EXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (int(userInput) < len(users)):
            open_chat()
        else:
            print("Wrong input. Please input the correct number.")
    
def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        send_to_server(username)
        send_to_server(password)
        msg = recive_from_server()
        print(msg)
        if(msg == "Logged in"):
            user_menu()
    
def user_menu():
    while True:
        userInput = input("Choose the option: \n1.Open chats\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (userInput== "1"):
            send_to_server(userInput)
            open_list()
        else:
            print("Wrong input. Please input the correct number.")




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