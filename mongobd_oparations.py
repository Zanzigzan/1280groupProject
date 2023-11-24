from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from dateutil.parser import parse


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
    print(f"Login execution starts {username} {password}")
    users = db["users"]

    logged_in = users.count_documents({"username": username, "password": password}) == 1
    
    if (logged_in):
        return "Logged in"
        
    else:
        return "Username or password are incorrect"

def insert_message(from_username, to_username, message):
    chats = db["chats"]
    users = [from_username, to_username]
    
    try:
        # Check if a chat exists, if not, create one
        chat = chats.find_one({"users": {"$all": users}})
        if not chat:
            chats.insert_one({
                "users": users,
                "messages": [],
            })
            message_index = 0  # Starting index for a new chat
        else:
            message_index = len(chat["messages"])  # Next index in existing chat

        # Add the new message with the index
        chats.update_many(
            {"users": {"$all": users}},
            {"$push": {
                "messages": {
                    "index": message_index,
                    "author": from_username,
                    "message": message,
                }
            }}
        )
        
    except Exception as e:
        print(e)
    
def create_chat(username):
    pass

def get_chats(username):
    chat_usernames = []
    chats = db["chats"]
    
    data = chats.find({"users": username})
    
    for row in data:
        chat_usernames.append(row['users'])
    
    return chat_usernames


def get_messages(username1, username2):
    chats = db["chats"]
    users = [username1, username2]

    try:
        # Fetch the chat document for the specified users
        chat_document = chats.find_one({"users": {"$all": users}})

        # If the chat document exists, return the messages array
        if chat_document:
            return chat_document["messages"]
        else:
            # Return an empty list if no chat exists between these users
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def delete_message(from_username, to_username, message_index):
    chats = db["chats"]
    users = [from_username, to_username]

    try:
        # Find the specific chat document
        chat = chats.find_one({"users": {"$all": users}})
        if chat and 0 <= message_index < len(chat["messages"]):
            # Update the specific message at the given index
            chat["messages"][message_index]["message"] = "***DELETED***"
            
            # Update the chat document in the database
            chats.update_one({"_id": chat["_id"]}, {"$set": {"messages": chat["messages"]}})
            print(f"Message at index {message_index} deleted.")
        else:
            print("Chat not found or invalid message index.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_user(username):
    chats = db["chats"]
    users = db["users"]

    # Delete all chats related to the user
    try:
        result = chats.delete_many({
            "users" : username
        })

        if result.deleted_count > 0:
            print(f"Chats for {username} deleted successfully") 
        else:
            print (f"No chats found for {username}")
        
    except Exception as e:
        print(e)
        return "An error has ocurred!"

    # Delete the user

    try:
        result = users.delete_one({
            "username" : username
        })
        if result.deleted_count > 0:
            return f"The user: {username} was deleted sucessfully!"
        else: 
            return f"The user: {username} wasn't deleted"
    except Exception as e: 
        print(e)
        return "An error has ocurred!"

def report_user(reported_user, reporter):
    reports = db["reports"]
    
    try:
        # Create a row if it does not exist
        if reports.count_documents({"reported user": reported_user}) == 0:
            reports.insert_one({
                "reported user": reported_user,
                "reports": [],
            })

        # Add reporter to reports if it is not already there 
        if not (reports.find_one({"reported user": reported_user,"reports": reporter})):
            reports.update_one(
                {"reported user": reported_user},
                {"$push": {"reports": reporter}}
            )
        
        # If at least 3 people reported delete this user
        if len(reports.get("reports", [])) == 3:
            delete_user()
            
    except Exception as e:
        print(e)
        return "An error has ocurred!"


def update_password(username, new_password):
    users = db["users"]
    user = users.find_one({"username": username})

    # Check if the user exists
    if user:
        try:
            # Update the password
            users.update_one({"username": username}, {"$set": {"password": new_password}})
            print(f"Password for {username} updated successfully")
            return "Password updated successfully"
        except Exception as e:
            print(e)
            return "Error updating password"
    else:
        return "User not found"


def update_username(username, new_username):
    users = db["users"]
    user = users.find_one({"username": username})

    # Check if the user exists
    if user:
        # Check if the new username is unique
        if not is_username_unique(new_username):
            return "The new username is already taken"

        try:
            # Update the username
            users.update_one({"username": username}, {"$set": {"username": new_username}})
            print(f"Username for {username} updated successfully to {new_username}")
            return "Username updated successfully"
        except Exception as e:
            print(e)
            return "Error updating username"
    else:
        return "User not found"




# TESTS
# register("Tom", "Tom123")

# print(is_username_unique("Tom"))
# print(is_username_unique("Tommm"))

# print(login("Tom", "Tom123"))
# print(login("Tom1", "Tom123"))
# print(login("Tom", "Tom133"))

# insert_message("Tom", "Victor", "Hello Victor! yoo test 1")
# delete_message("Tom", "Victor", 0)

# messages = get_messages('Tom', 'Victor')

# for message in messages:
#    print(f"{message['index']}\t{message['author']}:\t {message['message']}")

# print(get_chats("Tom"))



# report_user("Victor", "Tom")  

# update_password("Tom1", "Tom123")
# update_username("Tom1", "Tom")


# print(login("pawel", "pawel"))

# delete_user("VictorCampos")

