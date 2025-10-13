from copiar_arquivos import copiar_arquivos
from mover_arquivos import mover_arquivos

def execucao_backup(origem, destino, extensoes_permitidas):

    while True:

        print("\nDigite 'Copiar' para copiar os arquivos.")
        print("Digite 'Mover' para mover os arquivos.")
        acao = input("Ação desejada: ")

        if acao.lower() == 'copiar':
            copiar_arquivos(origem, destino, extensoes_permitidas)
            return
        
        elif acao.lower() == 'mover':
            mover_arquivos(origem, destino, extensoes_permitidas)
            return
        
        else:
            print("\nOpção inválida. Tente novamente.")