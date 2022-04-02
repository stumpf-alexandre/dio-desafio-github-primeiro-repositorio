# for x in range(100):
#     print(x)
#
# print('\n')
# for y in range(90, 101):
#     print(y)


# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo' .format(a))
# else:
#     print('número {} não é primo' .format(a))


# #imprime todos os numeros primos de 1 a 100
# for num in range(101):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)


# #imprime todos os numeros primos de 1 ao que é digitado
# a = int(input('Entre com um valor: '))
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)



# #implementando while
# a = 0
# while a <= 10:
#     print(a)
#     a += 1



#implementando media de nota com laço de repetição
a = int(input('Primeiro bimestre: '))
while a >10:
    a = int(input('Nota invalida. Entre com a nota do primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b >10:
    b = int(input('Nota invalida. Entre com a nota do segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c >10:
    c = int(input('Nota invalida. Entre com a nota do terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d >10:
    d = int(input('Nota invalida. Entre com a nota do quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))