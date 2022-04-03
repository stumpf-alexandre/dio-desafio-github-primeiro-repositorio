class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == True:
            self.ligada = False
            print('Televisão desligada')
        else:
            self.ligada = True
            print('Televisão ligada')

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# televisao = Televisao()
# # print(televisao.ligada)
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# # print(televisao.ligada)
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# # print(televisao.ligada)
# print('Televisão está ligada: {}'.format(televisao.ligada))
#
# print('Canal: {}'.format(televisao.canal))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.diminui_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.power()
# print('Canal: {}'.format(televisao.canal))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.diminui_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.power()


if __name__ == '__main__':#só é usado para testar o modulo no terminal do proprio PyCharm
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()