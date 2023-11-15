import socket
import threading
import sys

from server_app import *

# Global variables
clients_lock = threading.Lock()
clients = []
running = True


def handle_client(client_socket, client_address):
    global clients
    print(f"[+] New connection from {client_address}")

    with clients_lock:
        clients.append(client_socket)

    try:
        app(client_socket)

    except ConnectionResetError:
        print(f"[-] Connection reset by {client_address}")
    except Exception as e:
        print(f"[!] An exception occurred with {client_address}: {e}")
    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        client_socket.close()
        print(f"[-] Connection from {client_address} has been closed.")

def shutdown_server(server):
    global running, clients
    running = False
    # ensure that only one thread can execute the block of code under this statement at a time. 
    with clients_lock:
        for client in clients:
            try:
                client.send("Server is shutting down.".encode('utf-8'))
                client.close()
            except Exception as e:
                print(f"Error closing client socket: {e}")

    server.close()
    print("[*] Server has been shut down.")
    sys.exit()

def main():
    global running
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # reference: https://ianfinlayson.net/class/cpsc414/notes/03-sockets
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 12345)
    server.bind(server_address)
    server.listen(5)
    print('[*] Server is listening on ', server_address)

    # Thread to listen for shutdown command
    def listen_for_shutdown_command():
        global running
        while running:
            shutdown_command = input("Enter 'q' to quit: \n")
            if shutdown_command.lower() == 'q':
                shutdown_server(server)

    shutdown_thread = threading.Thread(target=listen_for_shutdown_command)
    shutdown_thread.daemon = True
    shutdown_thread.start()

    try:
        while running:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.daemon = True
            client_handler.start()
    except Exception as e:
        print(f"[!] An exception occurred: {e}")
    finally:
        if running:
            shutdown_server(server)

if __name__ == "__main__":
    main()