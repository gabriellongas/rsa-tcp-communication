
# Projeto de Comunicação Segura com Criptografia RSA

Este repositório contém um projeto de comunicação cliente-servidor utilizando criptografia RSA para garantir a troca segura de mensagens.

## Estrutura do Projeto

- **`rsa_utils.py`**: Implementa a geração de chaves pública e privada RSA, além de funções para criptografar e descriptografar mensagens.
- **`tcpclient.py`**: Implementa o cliente que se conecta a um servidor, troca chaves públicas e envia mensagens criptografadas.
- **`tcpserver.py`**: Implementa o servidor que se conecta a um cliente, troca chaves públicas e processa mensagens criptografadas.

## Funcionalidades

1. **Geração de Chaves RSA**:
   - As chaves são geradas utilizando números primos de 4096 bits para garantir a segurança das comunicações.

2. **Comunicação Cliente-Servidor**:
   - O cliente e o servidor trocam suas chaves públicas ao se conectarem.
   - O cliente envia uma mensagem criptografada ao servidor, que a processa e retorna uma resposta criptografada.

3. **Criptografia e Descriptografia**:
   - As mensagens são criptografadas usando a chave pública do destinatário e descriptografadas com a chave privada do destinatário.

## Como Executar

### Pré-requisitos

- Python 3.x
- Biblioteca `sympy` para manipulação de números primos.

### Passos para Execução

1. **Instale as dependências**:
   ```bash
   pip install sympy
   ```

2. **Inicie o Servidor**:
   - No terminal, execute:
     ```bash
     python tcpserver.py
     ```

3. **Inicie o Cliente**:
   - Em outro terminal, execute:
     ```bash
     python tcpclient.py
     ```

4. **Envie Mensagens**:
   - O cliente pedirá para você inserir uma mensagem. A mensagem será enviada ao servidor, criptografada, processada e a resposta será retornada ao cliente.

## Notas Técnicas

- O projeto usa criptografia RSA personalizada para demonstrar a troca segura de mensagens entre cliente e servidor.
- A segurança depende da complexidade das chaves RSA geradas com números primos grandes, garantindo a integridade e confidencialidade dos dados trocados.

## Contribuições

Sinta-se à vontade para enviar pull requests ou relatar problemas na seção de Issues.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
