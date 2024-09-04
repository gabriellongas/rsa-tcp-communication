from socket import *
from struct import *
from prime_utils import *
from rsa_utils import *
import ast

# Definição do endereço do servidor e porta
serverName = '127.0.0.1'
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)

def start_client():
    # Gera par de chaves pública e privada para o cliente
    public_key, private_key = generate_keypair(4096)

    # Conecta ao servidor
    clientSocket.connect((serverName, serverPort))

    # Envia a chave pública do cliente para o servidor
    keys = f"{public_key}".encode('utf-8')
    clientSocket.sendall(keys)

    # Recebe a chave pública do servidor
    encoded_server_key = clientSocket.recv(65000).decode('utf-8')
    server_public_key = ast.literal_eval(encoded_server_key)
    print('Public key received from server')

    # Envia uma mensagem para o servidor
    sentence = input("Input lowercase sentence: ")

    # Criptografa a mensagem usando a chave pública do servidor
    encrypted_message = encrypt(server_public_key, sentence)
    encoded_message = f"{encrypted_message}".encode('utf-8')
    clientSocket.sendall(encoded_message)

    # Recebe e descriptografa a resposta do servidor
    encoded_result = (clientSocket.recv(65000).decode('utf-8'))
    encrypted_result = ast.literal_eval(encoded_result)
    decrypted_result = decrypt(private_key, encrypted_result)
    print(f"Final message: {decrypted_result}")

    # Fecha a conexão
    clientSocket.close()

start_client()
