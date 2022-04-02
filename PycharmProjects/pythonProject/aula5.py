lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista_animal[1])

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

#ou

print(sum(lista))#sum ja faz a soma dos inteiros na lista

print(max(lista))#max traz o maior valor da lista

print(min(lista))#min traz o menor valor da lista

print(min(lista_animal))#min em uma lista de strings traz a menor letra da palavra

if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista')
    lista_animal.append('lobo')#append inclui mais uma string na lista
    print(lista_animal)

#multiplicando uma lista de strings
nova_lista = lista_animal * 3
print(nova_lista)

lista_animal.pop()#o pop remove uma string da lista
print(lista_animal)

lista_animal.pop()#o pop remove uma string da lista
print(lista_animal)

lista_animal.remove('elefante')#remove um elemento especifico
print(lista_animal)

lista_animal.append('lobo', 'elefante', 'arara')
lista_animal.sort()#ordena a lista de animais
lista.sort()#ordena a lista
print(lista_animal)
print(lista)

lista_animal.reverse()# reverse inverte a ordem da lista

lista_animal[0] = 'macaco'#troca os elementos de uma lista
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))#não se pode alterar os dados da lista na tupla, ela é imutavel
print(len(lista_animal))# o len conta quantos elementos temos na lista

tupla_animal = tuple(lista_animal)#o tuple converte uma lista
print(tupla_animal)

lista_numerica = list(tupla)#o list converte uma tupla em uma lista
print(lista_numerica)