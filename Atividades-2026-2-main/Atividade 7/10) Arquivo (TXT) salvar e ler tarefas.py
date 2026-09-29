while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        with open("tarefas.txt", "a") as arquivo:
            arquivo.write(tarefa + "\n")

        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\n--- TAREFAS ---")

        with open("tarefas.txt", "r") as arquivo:
            tarefas = arquivo.readlines()

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa.strip()}")

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")