import random
from sympy import isprime

# Função para gerar um número primo aleatório com 4096 bits
def generate_prime_candidate(length=4096):
    p = random.getrandbits(length)
    while not isprime(p):
        p = random.getrandbits(length)
    return p

# Função para verificar se um número é primo
def is_prime(num):
    return isprime(num)

#print(generate_prime_candidate(2048))
