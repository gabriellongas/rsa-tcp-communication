import random
from math import gcd
from prime_utils import generate_prime_candidate

# Função para gerar as chaves pública e privada com chaves de 4096 bits
def generate_keypair(length=4096):

    p = generate_prime_candidate(length)
    
    q = generate_prime_candidate(length)
    
    n = p * q
    
    phi = (p-1) * (q-1)
    
    e = random.randint(3, phi-1)
    while gcd(e, phi) != 1:
        e = random.randint(3, phi-1)

    d = mod_inverse(e, phi)
    
    return ((n, e), (n, d))

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

# Função para criptografar uma mensagem
def encrypt(public_key, plaintext):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_message

# Função para descriptografar uma mensagem
def decrypt(private_key, cipheredtext):
    n, d = private_key

    # Ensure that cipheredtext is a list of integers
    if not all(isinstance(ch, int) for ch in cipheredtext):
        raise ValueError("cipheredtext must be a list of integers.")

    decrypted_message = [chr(pow(int(ch), d, n)) for ch in cipheredtext]
    message = "".join(decrypted_message)
    return message
