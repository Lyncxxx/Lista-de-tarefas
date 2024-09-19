from validacao import *

class Tarefa:
    def __init__(self, descricao='sem descrição', status='Pendente', data_de_vencimento='sem data', prioridade='Baixa'):
        self.descricao = descricao
        self.status = status
        self.data_de_vencimento = data_de_vencimento
        self.prioridade = prioridade

    def __str__(self):
        return f'{self.descricao:<26} {self.status:>20} {self.data_de_vencimento:^15} {self.prioridade:<2}'

    def altera_status(self):
        while True:
            novo_status = str(input('Novo status: ')).strip().capitalize()
            if novo_status == self.status:
                print('Novo status não pode ser igual ao atual!')
            elif novo_status not in ['Concluída', 'Pendente']:
                print('Insira uma status válido! (Pendente ou Conclída)')
            else:
                self.status = novo_status
                print('Status alterado com sucesso!')
                break

    def alterar_prioridade(self):
        nova_prioridade =  leia_prioriadade('Nova prioridade: ')
        if nova_prioridade == self.prioridade:
            print('Nova prioridade não pode ser igual a atual!')
        elif nova_prioridade not in ['Alta', 'Média', 'Baixa']:
            print('Insira um prioridade válida!')
        else:
            self.prioridade = nova_prioridade
            print('Prioridade alterada com sucesso!')

    def alterar_descricao(self):
        nova_descricao = str(input('Nova descrição: '))
        self.descricao = nova_descricao
        print('Descrição alterada com sucesso!')

    def alterar_data(self):
        while True:
            nova_data = leia_data('Nova data[DD/MM/AAA]: ')
            if nova_data == self.data_de_vencimento:
                print('ERRO! Nova data não pode ser igual a atual!')
            else:
                self.data_de_vencimento = nova_data
                print('Data de vencimento alterada com sucesso!')
                break

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!')

    def remover_tarefa(self):
        while True:
            indice = int(input('Qual tarefa gostaria de remover? '))
            indice -= 1
            if 0 <= indice < len(self.tarefas):
                self.tarefas.pop(indice)
                print('Tarefa removida com sucesso!')
                break
            else:
                print('ERRO! Tarefa não encontrada.')

    def exibir_tarefas(self):
        if len(self.tarefas) == 0:
            print('A lista de tarefas está vazia!')
        else:
            print('-' * 80)
            print(f'{'N°  Descrição':<28} {'Status':>20} {'Data':>8} {'Prioridade':>19}')
            print('-'*80)
            for tarefa in self.tarefas:
                print(self.tarefas.index(tarefa) + 1, end=' - ')
                print(tarefa)

    def filtrar_status(self, status):
        for tarefa in self.tarefas:
            if tarefa.status == status:
                print(tarefa)

    def filtrar_prioridade(self, prioridade):
        for tarefa in self.tarefas:
            if tarefa.prioridade == prioridade:
                print(tarefa)