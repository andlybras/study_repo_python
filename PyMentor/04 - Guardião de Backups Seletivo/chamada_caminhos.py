def chamada_caminhos():
    origem = input("\nDigite o caminho da pasta de origem: ")
    destino = input("Digite o caminho da pasta de destino: ")

    origem = origem.strip().strip('"\'')
    destino = destino.strip().strip('"\'')

    print("\nIniciando o processo de backup...")
    
    print(f"\nPasta de origem: {origem}")
    print(f"Pasta de destino: {destino}")

    return origem, destino