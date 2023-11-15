import socket
import sys

from client_app import *

user_name = None  # Global variable to store the user's name

def main():
    global user_name
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print("You are now connected to the server.")

        app(client_socket)
        
    except ConnectionRefusedError:
        sys.exit("Server is not running.")
    except Exception as e:
        print(f"[!] An exception occurred: {e}")


if __name__ == "__main__":
    main()
