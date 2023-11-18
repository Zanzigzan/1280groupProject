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
        if chats.count_documents({"users": {"$all": users}}) == 0:
            chats.insert_one({
                "users": users,
                "messages": [],
            })
            

        chats.update_many(
            {"users": {"$all": users}},
            {"$push": {
                "messages": {"$each": [{
                    "author": from_username,
                    "message": message,
                    "date": datetime.now(),
                }]
                }}}
        )
        
    except Exception as e:
        print(e)
    

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


def delete_message(target_date_str):
    chats = db["chats"]

    # Convert the target_date string to a datetime object
    try:
        target_date = parse(target_date_str)
    except ValueError as e:
        print(f"Date parsing error: {e}")
        return

    try:
        # Update the messages in all chats
        result = chats.update_many(
            {"messages.date": target_date},
            {"$set": {"messages.$.message": "***DELETED***"}}
        )

        print(f"Number of documents modified: {result.modified_count}")
    except Exception as e:
        print(f"An error occurred: {e}")


# TESTS
# register("Tom", "Tom123")

# print(is_username_unique("Tom"))
# print(is_username_unique("Tommm"))

# print(login("Tom", "Tom123"))
# print(login("Tom1", "Tom123"))
# print(login("Tom", "Tom133"))

# insert_message("Tom", "Victor", "Hello Victor! yoo test 1")
# delete_message("2023-11-17T15:32:58.092+00:00")

# print(get_chats("Tom"))

# delete_message('2023-11-17 17:27:10.392000')

messages = get_messages('Tom', 'Victor')

for message in messages:
    print(f"{message['date']}\t{message['author']}:\t {message['message']}")
    
