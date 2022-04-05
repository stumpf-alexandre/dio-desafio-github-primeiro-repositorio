import os #importa o módulo ou biblioteca os(integra os programas e recursos do S.O.)

print('#' * 60) #imprimindo # 60 vezes
ip_ou_host = input('Digite o IP ou host a ser verificado: ') #criamos uma variavel que vai receber do usuário um IP
print('-' * 60) #imprime - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando system da biblioteca os - comando ping -n -num de pacotes que serão 6 {}
print('-' * 60) #imprime - 60 vezes