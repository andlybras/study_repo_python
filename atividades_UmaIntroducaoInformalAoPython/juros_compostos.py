def juros_compostos():

    investimento_inicial = float(input("Digite o valor do investimento inicial: "))
    taxa_juros_anual = float(input("Digite a taxa de juros anual sem %: "))
    tempo_investimento = int(input("Digite o tempo de investimento em anos: "))

    montante = investimento_inicial * (1 + taxa_juros_anual/100)**tempo_investimento

    print(montante)
