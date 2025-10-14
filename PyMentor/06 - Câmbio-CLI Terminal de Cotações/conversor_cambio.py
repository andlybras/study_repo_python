def coversor_cambio():

    print("\n" + "~"*30 + " Conversor de Câmbio " + "~"*30)
    print("\nEscolha a moeda que você deseja converter:")
    print("\n1. Dólar (USD)")
    print("2. Euro (EUR)")
    print("3. Libra Esterlina (GBP)")
    print("4. Iene Japonês (JPY)")

    escolha = input("\nDigite o número da moeda (1-4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
        return

    valor = float(input("Digite o valor que você deseja converter: "))

    taxas_cambio = {
        '1': 5.25,
        '2': 6.20,
        '3': 7.30,
        '4': 0.048,
    }

    taxa = taxas_cambio[escolha]
    valor_convertido = valor * taxa

    moedas = {
        '1': 'USD',
        '2': 'EUR',
        '3': 'GBP',
        '4': 'JPY'}
    
    print(f"{valor} {moedas[escolha]} é equivalente a R$ {valor_convertido:.2f}")

if __name__ == "__main__":
    coversor_cambio()