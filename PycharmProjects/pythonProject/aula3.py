a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))


# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')
#
#
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')
#
#
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')


# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número par')
# else:
#     print('Número impar')
#
#
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
#
# if a > b:
#    print('O maior número é: {}'.format(a))
# else:
#    print('O maior número é: {}'.format(b))
#
#
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > c and b > a:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))

print('Final do programa')