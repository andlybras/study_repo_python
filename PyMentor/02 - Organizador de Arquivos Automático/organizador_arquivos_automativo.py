import os
import shutil
from gerenciar_extensoes import extensoes, gerenciar_extensoes

def organizar_arquivos():
    print("\n" + "~"*30 + " Organizar Arquivos " + "~"*30)


def menu(gerenciar_extensoes, organizar_arquivos):
    print("\n" + "~"*30 + " Organizador de Arquivos Automático" + "~"*30)
    print("\n- Para Iniciar a Organização de Arquivos, Digite 'Iniciar'")
    print("- Para Gerenciar Extensões, Digite 'Gerenciar'")
    print("- Para Sair, Digite 'Sair'")

def programa(menu):

    while True:
        menu(gerenciar_extensoes, organizar_arquivos)

        acao_input = input("\nDigite a ação desejada: ")
        acao = acao_input.lower()

        if acao == "iniciar":
            organizar_arquivos()

        elif acao == "gerenciar":
            gerenciar_extensoes(extensoes)

        elif acao == "sair":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nAção inválida. Tente novamente.")

programa(menu)