# Exemplo basico socket (lado ativo)

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA)) 


entrada = input("Escreva o arquivo que sera aberto: ")
try:
    file = (open(entrada+'.txt','r'))
    print("arquivo aberto")
    a = file.read()
    
except:
    print("arquivo nao encontrado")

a = a.encode()
while(a != ("end".encode())):
    # envia uma mensagem para o par conectado
    sock.send(a)
    
    #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
    msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem

    # imprime a mensagem recebida
    print("\nA mensagem recebida do servidor passivo foi ",str(msg,  encoding='utf-8'))
    
    a = input("\nDeseja enviar mais uma? Escreva o nome do arquivo ou end para terminar: ")
    try:
        file = (open(entrada+'.txt','r'))
        print("arquivo aberto")
        a = file.read()
    except:
        print("arquivo nao encontrado")
    a = a.encode()
    

# encerra a conexao
sock.close() 

print("\nconexão encerrada!")
