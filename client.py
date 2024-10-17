import socket

soc1 = socket.socket()
soc1.connect(("localhost", 5000))  # Sending connection request to the server

while True:
    message = soc1.recv(1024).decode()  # Receiving the message sent by the server and storing it in the variable 'message'
    print(message)  # Print the received message
    
    message = input("Enter the message:")  # The client is getting some message to be sent to the server
    if message == "exit":  # Checking if the client wants to exit the chat room
        soc1.send(message.encode())  # Sending the exit message to the server
        break

    soc1.send(message.encode())  # If the message is not "exit", then the message is sent to the server
