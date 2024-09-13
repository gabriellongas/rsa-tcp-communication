from socket import *
from struct import *
from rsa_utils import *
import ast
import time

# Definição do endereço do servidor e porta
serverName = '127.0.0.1'
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)

def start_client():
    # Gera par de chaves pública e privada para o cliente
    print(f'[{time.ctime()}]Gerando chaves para client')
    public_key, private_key = generate_keypair(4096)
    print(f'[{time.ctime()}]Chaves criadas')

    # Conecta ao servidor
    print(f'[{time.ctime()}]Conectando com servidor')
    clientSocket.connect((serverName, serverPort))
    print(f'[{time.ctime()}]Client conectado com servidor')

    # Envia a chave pública do cliente para o servidor
    print(f'[{time.ctime()}]Enviando chave pública para o server')
    keys = f"{public_key}".encode('utf-8')
    clientSocket.sendall(keys)
    print(f'[{time.ctime()}]Chave pública enviada para o server')

    # Recebe a chave pública do servidor
    print(f'[{time.ctime()}]Aguardando chave pública do server')
    encoded_server_key = clientSocket.recv(65000).decode('utf-8')
    server_public_key = ast.literal_eval(encoded_server_key)
    print(f'[{time.ctime()}]Chave pública recebida')

    # Envia uma mensagem para o servidor
    sentence = input(f'[{time.ctime()}]Insira a mensagem para ser transformada: ')

    # Criptografa a mensagem usando a chave pública do servidor
    print(f'[{time.ctime()}]Criptografando mensagem')
    encrypted_message = encrypt(server_public_key, sentence)
    print(f'[{time.ctime()}]Enviando mensagem criptografada')
    encoded_message = f"{encrypted_message}".encode('utf-8')
    clientSocket.sendall(encoded_message)
    print(f'[{time.ctime()}]Mensagem enviada')

    # Recebe e descriptografa a resposta do servidor
    print(f'[{time.ctime()}]Aguardando mensagem criptografada do server')
    encoded_result = (clientSocket.recv(65000).decode('utf-8'))
    encrypted_result = ast.literal_eval(encoded_result)
    print(f'[{time.ctime()}]Mensagem recebida')

    print(f'[{time.ctime()}]Descriptografando mensagem do client')
    decrypted_result = decrypt(private_key, encrypted_result)
    print(f'[{time.ctime()}]Mensagem final: {decrypted_result}')

    # Fecha a conexão
    clientSocket.close()

start_client()
