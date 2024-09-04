import random
from sympy import isprime

# Função para gerar um número primo aleatório com 4096 bits
def generate_prime_candidate(length=4096):
    # Gera um número aleatório de 'length' bits
    p = random.getrandbits(length)
    # Continua gerando até que o número seja primo
    while not isprime(p):
        p = random.getrandbits(length)
    return p

# Função para verificar se um número é primo
def is_prime(num):
    # Verifica a primalidade do número usando a função isprime do sympy
    return isprime(num)
