# conjunto = {1, 2, 3, 4}#o conjunto não tem elasticidade pq não pode acrescentar outro elemento igual ao que ja tem dentro das chaves
# print(type(conjunto))
# conjunto.add(5)#adicionar um elemento no conjunto
# conjunto.discard(2)#discarta um elemento do conjunto
# print(conjunto)


conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
#faz a união entre os elementos dos conjuntos sem repetir os mesmos
conjunto_uniao = conjunto.union(conjunto2)
print('União:  {}'.format(conjunto_uniao))

#mostra quais elementos estavam repetidos na união dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

#mostra os elementos que possuem em um conjunto, mas não possuem no outro
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença entre conjunto 1 e 2: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre conjunto 2 e 1: {}'.format(conjunto_diferenca2))

#mostra tudo que só tem no elemento 1 e no elemento 2
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

#para ver se o conjunto 1 é subconjunto do conjunto 2 ou vice versa
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Conjunto A é um subconjunto do conjunto B: {}'.format(conjunto_subset))
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('Conjunto B é um subconjunto do conjunto A: {}'.format(conjunto_subset2))

#mostra se um conjunto é um super conjunto em relação ao outro conjunto
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('Conjunto A é um super conjunto do conjunto B: {}'.format(conjunto_superset))
conjunto_superset2 = conjunto_b.issuperset(conjunto_a)
print('Conjunto B é um super conjunto do conjunto A: {}'.format(conjunto_superset2))

#convertendo uma lista em um conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(type(conjunto_animais))
print('Conjunto: {}'.format(conjunto_animais))

#convertendo um conjunto em uma lista
lista_animais = list(conjunto_animais)
print(type(lista_animais))
print('Lista: {}'.format(lista_animais))