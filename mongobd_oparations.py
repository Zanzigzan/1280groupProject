from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


uri = "mongodb+srv://ProjectCoucou:THEproject@cluster0.ekjezah.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Coucou"]

# Utility functions
def is_username_unique(username):
    users = db["users"]
    
    return users.count_documents({"username": username}) == 0


# Functionality
def register(username, password):
    users = db["users"]

    if (is_username_unique(username)):
        try:
            
            users.insert_one({
                "username": username,
                "password": password,
            })
            
            print(f"User {username} created")
            
            return "User created successfully"
            
        except Exception as e:
            print(e)
            
            return "Error"
    else:
        return "User with this username already exists!"

def login(username, password):
    users = db["users"]

    logged_in = users.count_documents({"username": username, "password": password}) == 1
    
    if (logged_in):
        return "Logged in"
        
    else:
        return "Username or password are incorrect"

def insert_message(from_username, to_username, message):
    messages = db["messages"]
    
    try:
        messages.insert_one({
            "from_username": from_username,
            "to_username": to_username,
            "message": message,
            "date": datetime.now(),
            })
        
    except Exception as e:
        print(e)
    

def get_chats(username):
    # Checks all combinations of username + someone
    
    # Should return list of all chats with logged in user
    pass

def get_messages(username1, username2):
    # where username1 and username2 are both present
    messages = db["messages"]
    
    pass

def delete_message(date):
    # change the message with certain id 
    messages = db["messages"]
    
    # Just change message content to "*Deleted*"
    pass


# TESTS
# register("Tom", "Tom123")

# print(is_username_unique("Tom"))
# print(is_username_unique("Tommm"))

# print(login("Tom", "Tom123"))
# print(login("Tom1", "Tom123"))
# print(login("Tom", "Tom133"))

# insert_message("Tom", "Tom2", "Hello Tom2! Again")