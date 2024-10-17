import socket
soc1 = socket.socket()
print("socket created successfully.")

# Bind the hostname/IP and port number to listen on
tuple1 = ("localhost", 5000)
soc1.bind(tuple1)

# Listen to the incoming connections
soc1.listen(5)

print("Listening to the incoming connection....")
# While loop is executed as long as the connection is true

# conn object is used to refer to the connection created between 
# the server and the particular client
conn, client_addr = soc1.accept()  # accept() returns two pieces of information - client address and the connection object
print("Connected to the Client with IP address", client_addr)
# Using conn object, sending message to the particular client
conn.send("Hey! I am the server.".encode())

while True:
    message = conn.recv(1024).decode()  # Receiving message
    if message == "exit":
        print("The Client has Left the chat room.")
        print("The chat room has ended")
        break
    print(message)
    message = input("Enter the message:")
    conn.send(message.encode())
