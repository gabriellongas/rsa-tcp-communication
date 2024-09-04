from socket import *
from struct import *
from prime_utils import *
from rsa_utils import *
import ast

serverName = '127.0.0.1'
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)

def start_client():
    public_key, private_key = generate_keypair(4096)

    clientSocket.connect((serverName, serverPort))

    keys = f"{public_key}".encode('utf-8')
    clientSocket.sendall(keys)

    encoded_server_key = clientSocket.recv(65000).decode('utf-8')
    server_public_key = ast.literal_eval(encoded_server_key)
    print('Public key received from server')

    sentence = input("Input lowercase sentence: ")

    encrypted_message = encrypt(server_public_key, sentence)
    encoded_message = f"{encrypted_message}".encode('utf-8')
    clientSocket.sendall(encoded_message)

    encoded_result = (clientSocket.recv(65000).decode('utf-8'))
    encrypted_result = ast.literal_eval(encoded_result)
    
    decrypted_result = decrypt(private_key, encrypted_result)
    print(f"Final message: {decrypted_result}")

    clientSocket.close()

start_client()
