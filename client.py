import socket
import sys

from client_app import *

def main():
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
