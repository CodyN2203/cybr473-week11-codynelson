'''
Simple Client Data Transfer in the clear

In this example a connection is made between a client
and simple server running on the same machine over a
pre-defined and agreed upon port.

This client application will transfer a simple text message
to the server and receive a response back.
'''

import socket           # Import Python Standard Socket Library
import sys

print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555\n")

PORT = 5555             # Port Number of Server
HOST = '127.0.0.1'      # Server address (localhost)

client_socket = None # Initialize client_socket to None

try:
    # Create a Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the timeout before connecting so connect() is covered too.
    # settimeout only applies to calls made after it.
    client_socket.settimeout(10)

    print(f"Attempting Connection to: {HOST}:{PORT}")

    # Connect to the server
    client_socket.connect((HOST, PORT))

    print("Socket Connected...")
    print("Sending Messages to Server\n")

    # Send messages in a loop
    while True:
        user_message = input("Enter Message to Send or EXIT to End: ")

        # Encode and send the message
        encoded_message = user_message.encode("utf-8")
        client_socket.sendall(encoded_message)

        # Receive response from server
        server_response = client_socket.recv(2048)

        if not server_response:        # Empty response means the server closed the connection
            print("Server disconnected")
            break

        print(f"Server Response: {server_response.decode('utf-8')}\n")

        # Check if user wants to exit
        if user_message.lower() == 'exit':
            print("Closing connection...")
            break

    # Close the socket
    client_socket.close()
    print("Connection closed")

except socket.timeout:
    print(f"\nERROR: No response from {HOST}:{PORT} within 10 seconds")
    if client_socket is not None:
        client_socket.close()

except ConnectionRefusedError:
    print(f"\nERROR: Could not connect to server at {HOST}:{PORT}")
    print("Make sure the server is running first!")

except KeyboardInterrupt:
    print("\n\nClient stopped by user")
    if client_socket is not None:
        client_socket.close()

except Exception as err:
    print(f"Error: {err}")
    sys.exit(1)