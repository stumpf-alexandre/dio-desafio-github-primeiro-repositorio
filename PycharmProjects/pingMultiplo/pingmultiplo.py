import os #importa todas as dependencias do S.O.
import time # importa tempo para a o tempo de execução

with open('hosts.txt') as file: #abre um arquivo
    dump = file.read() #cria uma variavel dump, que vai receber o arquivo aberto para ler
    dump = dump.splitlines() #coloca o dump em linhas separadas

    for ip in dump:
        print('Verificando o IP: ', ip) #printa o IP
        print('-' * 60) #imprime - 60 vezes
        os.system('ping -n 2 {}'.format(ip)) #joga o IP no comando para enviar 2 pacotes
        print('-' * 60) #imprime - 60 vezes
        time.sleep(5) #da um tempo de execução