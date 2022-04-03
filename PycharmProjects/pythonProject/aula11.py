lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except ArithmeticError:
    print('Erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else: #serve para executar mais códigos caso não ocorra nem um exception
    print('Executa mais código quando não ocorre nem uma exceção')
finally: #serve para executar códigos obrigatórios
    print('Sempre executa, mesmo com erro no exception')
    arquivo.close()
    print('Fechando arquivo')