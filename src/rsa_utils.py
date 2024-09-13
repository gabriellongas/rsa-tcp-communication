import random
from Crypto.Util.number import getStrongPrime
from math import gcd

# Função para gerar as chaves pública e privada com chaves de 4096 bits
def generate_keypair(length=4096):
    # Gera dois números primos p e q
    p = getStrongPrime(length)
    q = getStrongPrime(length)
    # Calcula n como o produto de p e q
    n = p * q
    # Calcula phi (função totiente de Euler)
    phi = (p-1) * (q-1)
    # Escolhe e como um número aleatório co-primo com phi
    e = random.randint(3, phi-1)
    while gcd(e, phi) != 1:
        e = random.randint(3, phi-1)
    # Calcula o inverso modular de e (a chave privada)
    d = mod_inverse(e, phi)
    # Retorna a chave pública (n, e) e a chave privada (n, d)
    return ((n, e), (n, d))

# Função para calcular o inverso modular
def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

# Função para criptografar uma mensagem usando a chave pública
def encrypt(public_key, plaintext):
    n, e = public_key
    # Criptografa cada caractere da mensagem usando a fórmula de criptografia RSA
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_message

# Função para descriptografar uma mensagem usando a chave privada
def decrypt(private_key, cipheredtext):
    n, d = private_key
    # Garante que o texto cifrado seja uma lista de inteiros
    if not all(isinstance(ch, int) for ch in cipheredtext):
        raise ValueError("cipheredtext must be a list of integers.")
    # Descriptografa cada caractere da mensagem cifrada usando a fórmula de descriptografia RSA
    decrypted_message = [chr(pow(int(ch), d, n)) for ch in cipheredtext]
    message = "".join(decrypted_message)
    return message
