import ast
import time
global username
global password
global socket
global friendname

# Utility functions
def recive_from_server():
    message = socket.recv(1024).decode('utf-8')
    
    # print(f"Recived:{message}") # TEST
    
    return message


def send_to_server(message):
    # print(f"Sent:{full_message}")# TEST
    
    socket.send(message.encode('utf-8'))
    
    time.sleep(0.2)

#######################################################

def send_message():
    userInput = input("Type your message: ")
    send_to_server(userInput)
    print(f'{userInput} is sent to {friendname} successfully!')


def delete_message():
    get_messages()
    userInput = input("Type the index of the message you want to delete: ")
    send_to_server(userInput)
    print("Your message is successfully deleted")

# !!!! better to speficy the sender and receiver in database
def get_messages():
    messages = recive_from_server()
    str = messages[1:-1]
    msg_list = str.split(',')
    for message_object in msg_list:
        print(message_object)


def report_user():
    print("Do you want to report this user: ", friendname)
    userInput = input("1.Yes\n 2.No\n")
    send_to_server(userInput)


def open_chat():
    get_messages()
    while True:
        userInput = input("Choose the option: \n1.Check all messages\n2.Send a message\n3.Delete a message\n4.Report the user\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break

        if (userInput== "1"):
            send_to_server(userInput)
            get_messages()
        elif (userInput== "2"):
            send_to_server(userInput)
            send_message()      
        elif (userInput== "3"):
            send_to_server(userInput)
            delete_message()
        elif (userInput== "4"):
            send_to_server(userInput)
            report_user()
        else:
            print("Wrong input. Please input the correct number.")


def open_userlist():
    while True:
        users = recive_from_server()
        userpair_array = ast.literal_eval(users)
        if(len(userpair_array) == 0):
            print("You don't have any frined or chats yet!")
        else:
            print("Choose a friend:")

        user_array = []
        global friendname

        for name_pair in userpair_array:
            for name in name_pair:
                if name != username:
                    user_array.append(name)

        for count, user in enumerate(user_array):
            print(f'{count}. {user}')
        
        userInput = input("Exit\n") 

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        elif (int(userInput) < len(users)):
            send_to_server(userInput)
            friendname = user_array[int(userInput)]
            open_chat()
        else:
            print("Wrong input. Please input the correct number.")

def create_newchat():
    userInput = input("Enter a name that you want to add as friend: ")
    send_to_server(userInput)
    
    res = recive_from_server()
    print(res)


def change_username():
    userOldName = input("Your actual username: ")
    userInput = input("New username: ")
    print(f'Do you want to change your username to  {userInput}?')
    userconfirm = input("1.Yes\n2.No\n")
    if(userconfirm == "1"):
        send_to_server("yes")
        send_to_server(userInput)
        send_to_server(userOldName)
    else:
        send_to_server("no")
    
    print(recive_from_server())
    
    
   
def change_password():
    userName = input("Enter you user name: ")
    userInput1 = input("New password: ")
    userInput2 = input("Confirm your new password: ")
    if(userInput1 == userInput2):
        send_to_server("yes")
        send_to_server(userName)
        send_to_server(userInput1)

        result = recive_from_server()
        print(result)
    else: 
        print("Password doesn't match")
        send_to_server("no")
        

def user_menu():
    while True:
        userInput = input("Choose the option: \n1.Open chats\n2.Create a new chat\n3.Change your username\n4.Change your password\nEXIT\n")

        if userInput.upper() == 'EXIT':
            send_to_server(userInput)
            break
        
        if (userInput== "1"):
            send_to_server(userInput)
            open_userlist()
        elif(userInput== "2"):
            send_to_server(userInput)
            create_newchat()
        elif(userInput== "3"):
            send_to_server(userInput)
            change_username()
        elif(userInput== "4"):
            send_to_server(userInput)
            change_password()
        else:
            print("Wrong input. Please input the correct number.")

def login():
        global username
        global password
        
        username = input("Enter your username: ")
        send_to_server(username)
        
        password = input("Enter your password: ")
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