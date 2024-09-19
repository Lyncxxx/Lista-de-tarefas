from datetime import datetime

def leia_data(msg):
    while True:
        try:
            data = str(input(msg))
            datetime.strptime(data, '%d/%m/%Y')
        except:
            print('Formato de data invalido, deve ser DD/MM/AAAA')
        else:
            return data

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Informe um número válido!')
        else:
            return n

def leia_prioriadade(msg):
    lista_de_prioridades = ['Alta', 'Média', 'Baixa']
    while True:
        p = str(input(msg))
        if p in lista_de_prioridades:
            return p
        else:
            print('Insira uma prioridade válida! (Baixa, Média ou Alta)')
