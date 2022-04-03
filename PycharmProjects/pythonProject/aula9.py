import shutil
# #'w' cria, abre e escrever um arquivo
# arquivo = open('teste.txt', 'w')
#
# #escrever no arquivo
# arquivo.write('Minha primeira escrita')
#
# #fecha o arquivo
# arquivo.close()
#
# #'a' abre um arquivo existente e continua a escrever
# arquivo = open('teste.txt', 'a')
#
# #\n pula para a proxima linha e escreve no arquivo
# arquivo.write('\nSegunda linha')
#
# #fecha o arquivo
# arquivo.close()
#
# #'a' abre um arquivo existente e continua a escrever
# arquivo = open('teste.txt', 'a')
#
# #\n pula para a proxima linha e escreve no arquivo
# arquivo.write('\nTerceira linha')
#
# #fecha o arquivo
# arquivo.close()

def escrever_arquivo(texto):
    # #gerando o arquivo no diretório que voce quiser
    # diretorio = 'C:/curso/desafioGit-GitHub/dio-desafio-github-primeiro-repositorio/PycharmProjects/teste.txt'
    # arquivo = open(diretorio, 'w')

    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota) #passa uma string
    aluno_nota = aluno_nota.split('\n') #transforma em uma lista quando houver quebra de linha ou seja '\n'
    #print(aluno_nota) #passa uma lista
    lista_media = []
    for x in aluno_nota:
        linsta_notas = x.split(',') #transforma em uma lista quando houver virgula ou seja ','
        aluno = linsta_notas[0]
        linsta_notas.pop(0) #retira o item da posição 0 da lista
        print(aluno)
        print(linsta_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(linsta_notas))
        lista_media.append({aluno:media(linsta_notas)})
    return lista_media

#copia um arquivo para outro diretório
def copia_arquivo(nome_arquivo):
    # import shutil #importação de uma biblioteca imbutida no Python
    shutil.copy(nome_arquivo, 'C:/curso/desafioGit-GitHub/dio-desafio-github-primeiro-repositorio/PycharmProjects/')

#move um arquivo para outro diretório
def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/curso/desafioGit-GitHub/dio-desafio-github-primeiro-repositorio/PycharmProjects/')

if __name__ == '__main__':
    #escrever_arquivo('primeira linha.\n')
    #atualizar_arquivo('segunda linha.\n')
    #ler_arquivo('teste.txt')
    #aluno = 'Rafael, 10, 10, 5, 5\n'
    #aluno = 'Felipe, 7, 8, 5, 6\n'
    #aluno = 'Galleani, 7, 8, 5, 6\n'
    #aluno = 'Cesar, 7, 9, 3, 8'
    #atualizar_arquivo('nota.txt', aluno)
    # media_notas('nota.txt')
    # lista_media = media_notas('nota.txt')
    # print(lista_media)
    # copia_arquivo('nota.txt')
    mover_arquivo('nota.txt')