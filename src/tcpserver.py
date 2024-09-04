from socket import *
from struct import *
from prime_utils import *
from rsa_utils import *
import ast

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)

def start_server():
    public_key, private_key = generate_keypair(4096)

    connectionSocket, addr = serverSocket.accept()
    print("Server listening to client\n")

    encoded_client_key = connectionSocket.recv(65000).decode('utf-8')
    client_public_key = ast.literal_eval(encoded_client_key)
    print("Public key received from client")

    keys = f"{public_key}".encode('utf-8')
    connectionSocket.sendall(keys)

    encoded_message = connectionSocket.recv(65000).decode('utf-8')
    message = ast.literal_eval(encoded_message)
    #print("Received From Client (encrypted): ", received)

    decrypted_message = decrypt(private_key, message)
    capitalizedSentence = decrypted_message.upper()

    encrypted_result = encrypt(client_public_key, capitalizedSentence)

    encoded_result = f"{encrypted_result}".encode('utf-8')
    connectionSocket.sendall(encoded_result)

    connectionSocket.close()

start_server()
