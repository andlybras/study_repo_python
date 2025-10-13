import os

def chamada_caminhos():

    while True:
        origem = input("\nDigite o caminho da pasta de origem: ").strip().strip('"\'')

        if os.path.isdir(origem):
            break

        else:
            print(f"ERRO: A pasta de origem '{origem}' não foi encontrada. Tente novamente.")

    while True:
        destino = input("Digite o caminho da pasta de destino: ").strip().strip('"\'')

        if os.path.isdir(destino):
            break
        
        else:
            print(f"ERRO: A pasta de destino '{destino}' não foi encontrada. Tente novamente.")

    print("\nCaminhos validados. Iniciando o processo de backup...")
    print(f"\nPasta de origem: {origem}")
    print(f"Pasta de destino: {destino}")

    return origem, destino