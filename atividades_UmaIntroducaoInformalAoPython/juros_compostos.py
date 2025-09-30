def juros_compostos():

    investimento_inicial = float(input("\nDigite o valor do investimento inicial: "))
    taxa_juros_anual = float(input("\nDigite a taxa de juros anual sem %: "))
    tempo_investimento = int(input("\nDigite o tempo de investimento em anos: "))

    montante = investimento_inicial * (1 + taxa_juros_anual/100)**tempo_investimento

    print("")
    print(montante)
