from chamada_caminhos import chamada_caminhos
from execucao_backup import execucao_backup

extensoes_permitidas = ['.pdf']

def menu_guardiao_backups():

    while True:
        print("\n" + "~"*30 + " Guardião de Backups  " + "~"*30)
        print("\nPara iniciar o backup, digite 'Iniciar'")
        print("Para sair, digite 'Sair'")
        opcao_menu = input("\nDigite a opção desejada: ")

        if opcao_menu.lower() == 'iniciar':
            origem, destino = chamada_caminhos()
            execucao_backup(origem, destino, extensoes_permitidas)
            print("\nBackup concluído com sucesso!\n")
            return
        
        elif opcao_menu.lower() == 'sair':
            print("\nPrograma Encerrado. Até mais!\n")
            return
        
        else:
            print("\nOpção inválida. Tente novamente.")

menu_guardiao_backups()