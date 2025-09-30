def contator_vogais():
    palavra = input("\nDigite uma palavra/frase para contar as vogais: ")
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1
            
    print(f"\nA palavra possui {contador} vogais.")