def gerador_acronimos():
    frase = input("\nDigite uma frase para gerar o acrônimo: ")
    palavras_excluidas = ['de', 'da', 'do', 'das', 'dos', 'e', 'ou', 'para', 'com', 'sem', 'em', 'uma', 'um', 'a', 'o', 'as', 'os']
    frase_limpa = frase.lower()
    palavras = frase_limpa.split()

    acronimo_lista = [
        palavra[0] 
        for palavra in palavras 
        if palavra not in palavras_excluidas and len(palavra) > 0
    ]

    acronimo = "".join(acronimo_lista)
    
    print(f"\nO acrônimo é: {acronimo.upper()}")