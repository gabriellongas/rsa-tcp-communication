from socket import *
from struct import *
from prime_utils import *
from rsa_utils import *
import ast

# Definição do endereço do servidor e porta
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)

def start_server():
    # Gera par de chaves pública e privada para o servidor
    public_key, private_key = generate_keypair(4096)

    # Aceita a conexão do cliente
    connectionSocket, addr = serverSocket.accept()
    print("Server listening to client")

    # Recebe a chave pública do cliente
    encoded_client_key = connectionSocket.recv(65000).decode('utf-8')
    client_public_key = ast.literal_eval(encoded_client_key)
    print("Public key received from client")

    # Envia a chave pública do servidor para o cliente
    keys = f"{public_key}".encode('utf-8')
    connectionSocket.sendall(keys)

    # Recebe e descriptografa a mensagem do cliente
    encoded_message = connectionSocket.recv(65000).decode('utf-8')
    message = ast.literal_eval(encoded_message)
    decrypted_message = decrypt(private_key, message)
    capitalizedSentence = decrypted_message.upper()

    # Criptografa a resposta e envia de volta ao cliente
    encrypted_result = encrypt(client_public_key, capitalizedSentence)
    encoded_result = f"{encrypted_result}".encode('utf-8')
    connectionSocket.sendall(encoded_result)

    # Fecha a conexão
    connectionSocket.close()

start_server()
