import socket  # noqa: F401
import threading


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
     # wait for client

    while True:
        connection, _ = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(connection,))
        thread.start()


def handle_client(connection):
    while True:
        data = connection.recv(1024)  # receive data from client
        if not data:
            break
        connection.sendall(b"+PONG\r\n")  # send response to client


if __name__ == "__main__":
    main()
