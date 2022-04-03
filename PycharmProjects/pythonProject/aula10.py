from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))

    data_atual_str = data_atual.strftime('%d/%m/%y')#transforma os dados em string no formato das diretrizes do Python
    print(data_atual_str)
    print(type(data_atual_str))

    data_atual_str = data_atual.strftime('%d/%m/%Y')#transforma os dados em string no formato das diretrizes do Python
    print(data_atual_str)
    print(type(data_atual_str))

    data_atual_str = data_atual.strftime('%A %d %B %Y')#transforma os dados em string no formato das diretrizes do Python
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(type(data_atual))
    data_atual_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(data_atual_str)
    print(type(data_atual_str))
    data_atual_str = data_atual.strftime('%c')
    print(data_atual_str)
    print(type(data_atual_str))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])

    tupla2 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(tupla2[data_atual.month])

    data_criada = datetime(2022, 4, 2, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    #transformando data em string em datetime
    data_string = '02/04/2022 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()