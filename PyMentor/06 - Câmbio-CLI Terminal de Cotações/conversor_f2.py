import requests
from moedas import moedas

def conversor_f2(moedas):

    while True:
        
        escolha_moeda_converter = input("Digite a moeda a ser convertida (ex: USD, EUR, BRL): ").upper()

        if escolha_moeda_converter not in moedas.keys():
            print("Moeda inválida ou não disponível. Tente novamente.")
            continue

        while True:
            escolha_moeda_referencia = input("Digite a moeda de referência (ex: USD, EUR, BRL): ").upper()

            if escolha_moeda_referencia not in moedas.keys():
                print("Moeda inválida ou não disponível. Tente novamente.")
                continue

            else:
                break
        
        while True:
            valor_converter = input(f"Digite o valor em {escolha_moeda_converter} a ser convertido: ")

            try:
                valor_converter = float(valor_converter)

                if valor_converter < 0:
                    print("O valor deve ser positivo. Tente novamente.")
                    continue

                else:
                    break

            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue
        
        url = f"https://v6.exchangerate-api.com/v6/7ebe4375447280ba2157a10c/latest/{escolha_moeda_converter}"
        resposta = requests.get(url)
        dados = resposta.json()
        taxa_cambio = dados['conversion_rates'][escolha_moeda_referencia]
        valor_convertido = valor_converter * taxa_cambio
        print(f"\n{valor_converter:.2f} {escolha_moeda_converter} equivalem a {valor_convertido:.2f} {escolha_moeda_referencia}.\n")
        break

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