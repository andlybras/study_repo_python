import requests
import moedas

def conversor_f2(moedas):
    print("")

def menu_conversor_f2(moedas):

    while True:
        print("\n" + "~"*30 + " Conversor de Câmbio " + "~"*30)
        print("\n* 1 - Realizar Conversão")
        print("* 2 - Consultar Moedas Disponíveis")
        print("* 3 - Sair")
        
        escolha = input("\nDigite a opção desejada: ")

        if escolha == '1':
            conversor_f2(moedas)
            continue

        elif escolha == '2':
            moedas.listar_moedas()
            continue

        elif escolha == '3':
            print("Programa encerrado.")
            return

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_conversor_f2(moedas)