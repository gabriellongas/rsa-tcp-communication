from socket import *
from struct import *
from rsa_utils import *
import ast
import time

# Definição do endereço do servidor e porta
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)

def start_server():
    # Gera par de chaves pública e privada para o servidor
    print(f'[{time.ctime()}]Gerando chaves para server')
    public_key, private_key = generate_keypair(4096)
    print(f'[{time.ctime()}]Chaves criadas')

    # Aceita a conexão do cliente
    print(f'[{time.ctime()}]Aguardando conexão com client')
    connectionSocket, addr = serverSocket.accept()
    print(f'[{time.ctime()}]Server ouvindo o client')

    # Recebe a chave pública do cliente
    print(f'[{time.ctime()}]Aguardando chave pública do client')
    encoded_client_key = connectionSocket.recv(65000).decode('utf-8')
    client_public_key = ast.literal_eval(encoded_client_key)
    print(f'[{time.ctime()}]Chave pública recebida')

    # Envia a chave pública do servidor para o cliente
    print(f'[{time.ctime()}]Enviando chave pública para o client')
    keys = f"{public_key}".encode('utf-8')
    connectionSocket.sendall(keys)
    print(f'[{time.ctime()}]Chave pública enviada para o server')

    # Recebe e descriptografa a mensagem do cliente
    print(f'[{time.ctime()}]Aguardando mensagem criptografada do client')
    encoded_message = connectionSocket.recv(65000).decode('utf-8')
    message = ast.literal_eval(encoded_message)
    print(f'[{time.ctime()}]Mensagem recebida')

    print(f'[{time.ctime()}]Descriptografando mensagem do client')
    decrypted_message = decrypt(private_key, message)
    print(f'[{time.ctime()}]Mensagem descriptografada: {decrypted_message}')

    capitalizedSentence = decrypted_message.upper()
    print(f'[{time.ctime()}]Mensagem transformada: {capitalizedSentence}')

    # Criptografa a resposta e envia de volta ao cliente
    print(f'[{time.ctime()}]Criptogradando mensagem transformada')
    encrypted_result = encrypt(client_public_key, capitalizedSentence)
    encoded_result = f"{encrypted_result}".encode('utf-8')
    print(f'[{time.ctime()}]Enviando mensagem criptografada para o client')
    connectionSocket.sendall(encoded_result)
    print(f'[{time.ctime()}]Mensagem enviada')

    # Fecha a conexão
    connectionSocket.close()

start_server()
