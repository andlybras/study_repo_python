def pares_impares():
    pares = []
    impares = []

    while True:

        print("-"*10 + " Separador de Pares e Ímpares " + "-"*10)
        entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            print(f"\nNúmeros pares: {pares}")
            print(f"\nNúmeros ímpares: {impares}")
            print("\nPrograma Encerrado")
            break
        
        try:
            numero = int(entrada)

            if numero % 2 == 0:
                pares.append(numero)
                
            else:
                impares.append(numero)

        except ValueError:
            print("Entrada inválida. Tente novamente.")