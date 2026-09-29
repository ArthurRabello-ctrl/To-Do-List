tarefas = []

while True:
    print('\n1 - Adicionar')
    print('2 - Listar')
    print('3 - Concluir')
    print('4 - Remover')
    print('0 - Sair')
    opcao = input('Escolha: ')

    if opcao == "1":
        titulo = input('Nova tarefa: ')
        tarefas.append({'titulo': titulo, 'feita': False})

    elif opcao == "2":
        if not tarefas:
            print('Não há tarefas!')
        for i, tarefa in enumerate(tarefas, start=1):
            marca = '[x]' if tarefa['feita'] else '[ ]'
            print(f"{i}. {marca} {tarefa['titulo']}")

    elif opcao == "3":
        numero = int(input('Número da tarefa: '))
        tarefas[numero - 1]['feita'] = True

    elif opcao == "4":
        numero = int(input('Número da tarefa: '))
        tarefas.pop(numero - 1)

    elif opcao == "0":
        break

    else:
        print('Opção inválida.')