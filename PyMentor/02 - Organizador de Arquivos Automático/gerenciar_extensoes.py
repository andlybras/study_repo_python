extensoes = {
    "Imagens": [".jpg", ".png", ".gif"],
    "Documentos": [".pdf", ".doc", ".txt"],
    "Audios": [".mp3"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Arquivos": [".zip"],
    "Outros": []
}

def mostrar_categorias(extensoes):
    print("\nOs grupos de extensões são: ")
    print("")

    for grupo_extensoes in extensoes.keys():
        if grupo_extensoes != "Outros":
            print(f"- {grupo_extensoes}")

def gerenciar_extensoes(extensoes):
    
    print("\n" + "~"*30 + " Gerenciar Extensões " + "~"*30)

    while True:
        mostrar_categorias(extensoes)

        while True:
            visualizar_extensoes_input = input("\nDigite o grupo do qual você quer visualizar as extensões cadastradas (ou 'Voltar' para retornar ao menu anterior): ")
            visualizar_extensoes = visualizar_extensoes_input.title()

            if visualizar_extensoes in extensoes.keys():
                print(extensoes[visualizar_extensoes])

                while True:
                    gerenciar_extensao = input("\nDigite 'Adicionar' para inserir uma nova extensão, 'Excluir' para remover uma extensão, ou 'Voltar' para retornar ao menu anterior: ").lower()

                    if gerenciar_extensao == "adicionar":
                        nova_extensao = input("\nDigite a nova extensão: ")
                        if not nova_extensao.startswith('.'):
                            nova_extensao = '.' + nova_extensao

                        if nova_extensao in extensoes[visualizar_extensoes]:
                            print(f"\nExtensão '{nova_extensao}' já está cadastrada. Tente novamente.")
                            continue

                        extensoes[visualizar_extensoes].append(nova_extensao)
                        print(f"\nExtensão adicionada com sucesso!\n{extensoes[visualizar_extensoes]}")

                    elif gerenciar_extensao == "excluir":
                        extensao_remover = input("\nDigite a extensão que deseja remover: ")
                        if not extensao_remover.startswith('.'):
                            extensao_remover = '.' + extensao_remover

                        if extensao_remover in extensoes[visualizar_extensoes]:
                            extensoes[visualizar_extensoes].remove(extensao_remover)
                            print(f"\nExtensão removida com sucesso!\n{extensoes[visualizar_extensoes]}")

                        else:
                            print(f"\nExtensão '{extensao_remover}' não encontrada. Tente novamente.")

                    elif gerenciar_extensao == "voltar":
                        mostrar_categorias(extensoes)
                        break

                    else:
                        print("\nOpção inválida. Tente novamente.")

            elif visualizar_extensoes_input.lower() == "voltar":
                return

            else:
                print("\nGrupo não encontrado. Tente novamente.")

if __name__ == "__main__":
    gerenciar_extensoes(extensoes)