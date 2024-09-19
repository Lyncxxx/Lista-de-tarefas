import sys
from validacao import *
from sistema import *

def main():
    while True:
        opcao = leia_int('''--------------------------------
        Lista de tarefas
--------------------------------
[1] Ver lista de tarefas
[2] Adicionar tarefa
[3] Remover tarefa
[4] Modificar tarefa
[5] Sair do sitema
> ''')
        if opcao == 1:
            lista_de_tarefas.exibir_tarefas()

        elif opcao == 2:
            descricao = str(input('Descrição: '))
            data = leia_data('Data de vencimento[DD/MM/AAA]: ')
            prioridade = leia_prioriadade('Prioridade: ')
            tarefa = Tarefa(descricao, 'Pendente', data, prioridade)
            lista_de_tarefas.adicionar_tarefa(tarefa)

        elif opcao == 3:
            tamanho_da_lista = len(lista_de_tarefas.tarefas)
            if tamanho_da_lista != 0:
                lista_de_tarefas.remover_tarefa()
            else:
                print('ERRO! A lista está vazia, não é possível remover tarefa.')

        elif opcao == 4:
            tamanho_da_lista = len(lista_de_tarefas.tarefas)
            if tamanho_da_lista != 0:
                while True:
                    indice = leia_int('Qual tarefa gostaria de modificar? ')
                    indice -= 1
                    if 0 <= indice < tamanho_da_lista:
                        while True:
                            res = leia_int('''[1] Alterar descrição
    [2] Alterar data
    > ''')
                            if res in range(1, 3):
                                break
                            else:
                                print('Informe uma opção válida! (Tente um número entre 1 e 2)')
                        for tarefa in lista_de_tarefas.tarefas:
                            if indice == lista_de_tarefas.tarefas.index(tarefa):
                                if res == 1:
                                    tarefa.alterar_descricao()
                                elif res == 2:
                                    tarefa.alterar_data()
                        break
                    else:
                        print('ERRO! Tarefa não encontrada!')
            else:
                print('Insira uma tarefa a lista antes de tentar modificá-la!')

        elif opcao == 5:
            print('Até logo!')
            sys.exit()

        else:
            print('Informe uma opção válida! (Tente um número entre 1 e 5)')


if __name__ == '__main__':
    lista_de_tarefas = ListaDeTarefas()
    main()