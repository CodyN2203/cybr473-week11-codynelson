'''
Simple Server to receive data from client and respond

In this example a connection is made between a client
and simple server running on the same machine over a
pre-defined and agreed upon port.

This server application will wait for a connection request
over a pre-defined port.
Once a connection is established the server will receive data sent
over the port, display the contents of the received data, and send
a response back to the client.

When a client disconnects, the server goes back to waiting for the
next one. Stop the server with Ctrl+C.
'''

import socket       # import Python Standard Socket Library
import sys

print("Server Starting up\n")

server_socket = None
client_connection = None

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP Socket

    local_host = '127.0.0.1'       # Bind to localhost
    local_port = 5555              # Specify a local Port
                                   # to accept connections on

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse

    server_socket.bind((local_host, local_port))  # Bind socket to localhost

    server_socket.listen(1)        # Listen for connections

    print(f'Server listening on {local_host}:{local_port}')
    print('Waiting for Connection Request\n')

    while True:                    # Keep serving clients until Ctrl+C

        ''' Wait for a connection request
            Note this is a synchronous call meaning the program will halt until
            a connection is received. Once a connection is received
            we will accept the connection and obtain the
            address of the connecting client
        '''

        client_connection, client_address = server_socket.accept()

        print(f"Connection Received from Client: {client_address[0]}:{client_address[1]}\n")

        while True:
            received_bytes = client_connection.recv(2048)  # Wait for Data (max 2048 bytes)

            if not received_bytes:                         # Client disconnected
                print("Client disconnected")
                break

            received_message = received_bytes.decode('utf-8')  # Decode bytes to string
            print(f"Received: {received_message}")

            # Send a response back to the client
            response_message = "Server received your message!"

            if "hello" in received_message.lower():
                response_message += f" Hello, {client_address[0]}!"

            client_connection.sendall(response_message.encode('utf-8'))
            print(f"Sent response: {response_message}\n")

            if received_message.strip().lower() == 'exit':
                print("Client ended the session")
                break

        client_connection.close()      # Done with this client
        client_connection = None
        print("Waiting for Connection Request\n")

except KeyboardInterrupt:
    print("\n\nServer stopped by user")

except Exception as err:
    print(f"Error: {err}")
    sys.exit(1)

finally:
    if client_connection is not None:
        client_connection.close()      # Close client connection
    if server_socket is not None:
        server_socket.close()          # Close server socket