def lista_compras():
    lista = []

    while True:
        print("#"*10 + " Minha Lista de Compras " + "#"*10)
        print("\n1 - Visualizar lista")
        print("2 - Adicionar item")
        print("3 - Remover item")
        print("4 - Sair")
        escolha = input("\nDigite o número da opção desejada: ")

        try:
            if escolha == "1":
                print(lista)
            elif escolha == "2":
                novo_item = input("\nDigite o item que deseja adicionar: ")
                lista.append(novo_item)
            elif escolha == "3":
                item_removido = input("\nDigite o item que deseja remover: ")
                if item_removido in lista:
                    lista.remove(item_removido)
                else:
                    print("Item não encontrado na lista.")
            elif escolha == "4":
                print(f"\nSua lista de compras é:\n\n{lista}")
                print()
                print("\nPrograma Encerrado")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except:
            print("Opção inválida. Tente novamente.")