import os
import shutil
from gerenciar_extensoes import extensoes, gerenciar_extensoes

def organizar_arquivos(extensoes):
    caminho_bruto = input("\nDigite o caminho da pasta que deseja organizar: ")
    caminho_pasta = caminho_bruto.strip().strip('"> ')
    print("\nIniciando organização de arquivos...")

    itens_pasta = os.listdir(caminho_pasta)

    for grupo_extensoes in extensoes.keys():
        caminho_grupo_extensoes = os.path.join(caminho_pasta, grupo_extensoes)

        if caminho_grupo_extensoes not in itens_pasta:
            os.mkdir(caminho_grupo_extensoes)

    caminho_do_log = os.path.join(caminho_pasta, "log_organizacao.txt")
    with open(caminho_do_log, "a") as log:

        for item in itens_pasta:
            caminho_completo_do_item = os.path.join(caminho_pasta, item)
            if os.path.isdir(caminho_completo_do_item):
                continue

            nome_item, extensao_item = os.path.splitext(item)

            for grupo_extensoes, extensoes_validas in extensoes.items():
                if extensao_item in extensoes_validas:
                    caminho_destino = os.path.join(caminho_pasta, grupo_extensoes)
                    shutil.move(caminho_completo_do_item, caminho_destino)
                    mensagem = (f"INFO: Arquivo '{item}' movido para a pasta {grupo_extensoes}.\n")
                    log.write(mensagem)
                    break

            else:
                caminho_destino = os.path.join(caminho_pasta, "Outros")
                shutil.move(caminho_completo_do_item, caminho_destino)
                mensagem = (f"INFO: Arquivo '{item}' movido para a pasta 'Outros'.\n")
                log.write(mensagem)

        print("\nOrganização concluída!")

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
            organizar_arquivos(extensoes)

        elif acao == "gerenciar":
            gerenciar_extensoes(extensoes)

        elif acao == "sair":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nAção inválida. Tente novamente.")

programa(menu)