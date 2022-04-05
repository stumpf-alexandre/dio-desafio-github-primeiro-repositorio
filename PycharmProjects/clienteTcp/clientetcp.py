import socket
#controla a abertura, fechamento, e sincronização de conexões direto com a placa de rede
import sys
#fornece o acesso a algumas variaveis e algumas funções que tem forte interação com o Python

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " - Porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel conectar no Host: " + HostAlvo + " - Porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == '__main__':
    main()