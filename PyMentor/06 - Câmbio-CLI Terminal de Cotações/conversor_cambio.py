def coversor_cambio():

    taxas_cambio = {
        '1':  [5.25, 'USD'],
        '2':  [6.20, 'EUR'],
        '3':  [7.30, 'GBP'],
        '4':  [0.048, 'JPY'],
    }

    print("\n" + "~"*30 + " Conversor de Câmbio " + "~"*30)
    print("\nEscolha a moeda que você deseja converter:")

    for escolha, taxa_moeda in taxas_cambio.items():
        for taxa, moeda in [taxa_moeda]:
            print(f"{escolha}. {moeda} - Taxa de câmbio: R$ {taxa}")

    escolha = input("\nDigite sua opção: ")

    while True:

        if escolha not in taxas_cambio.keys():
            print("Opção inválida.")
            break
        
        else:
            valor = float(input("Digite o valor que você deseja converter: "))
            taxa = taxas_cambio[escolha][0]
            valor_convertido = valor * taxa        
            print(f"{valor} {taxas_cambio[escolha][1]} é equivalente a R$ {valor_convertido:.2f}")
            break

if __name__ == "__main__":
    coversor_cambio()