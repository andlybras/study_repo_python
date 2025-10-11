import os
import shutil

extensoes_permitidas = ['.pdf']

def guardiao_backups():

    while True:
        print("\n" + "~"*30 + " Guardião de Backups  " + "~"*30)
        print("\nPara iniciar o backup, digite 'Iniciar'")
        print("Para sair, digite 'Sair'")
        opcao_menu = input("\nDigite a opção desejada: ")

        if opcao_menu.lower() == 'iniciar':
            print()
        
        elif opcao_menu.lower() == 'sair':
            print("\nPrograma Encerrado. Até mais!\n")
            return
        
        else:
            print("\nOpção inválida. Tente novamente.")

guardiao_backups()