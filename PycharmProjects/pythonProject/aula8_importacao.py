from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    #acessando classe Televisão
    televisao = Televisao()

    #acessando classe Calculadora1
    calculadora = Calculadora(5, 10)

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {}'.format(total_letras))