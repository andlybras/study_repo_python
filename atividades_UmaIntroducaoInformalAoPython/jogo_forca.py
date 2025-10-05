import random

def jogo_forca():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "interface", "biblioteca"]
    palavra_secreta = random.choice(palavras)
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    print("\n" + "#"*10 + " Jogo da Forca " + "#"*10)
    print("Adivinhe a palavra secreta!")

    while tentativas > 0:
        palavra_mostrada = ""
        for letra in palavra_secreta:
            if letra in letras_corretas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "_ "
        
        print("\nPalavra:", palavra_mostrada.strip())
        print(f"Tentativas restantes: {tentativas}")
        if letras_erradas:
            print(f"Letras erradas: {', '.join(sorted(letras_erradas))}")

        if "_" not in palavra_mostrada:
            print("\nParabéns! Você adivinhou a palavra!")
            print(f"A palavra era: '{palavra_secreta}'")
            break

        palpite = input("Digite uma letra: ").lower()

        if not palpite.isalpha() or len(palpite) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra_secreta:
            letras_corretas.add(palpite)
            print("Bom palpite!")
        else:
            letras_erradas.add(palpite)
            tentativas -= 1
            print("Letra não encontrada.")

    if tentativas == 0:
        print("\nVocê perdeu! As tentativas acabaram.")
        print(f"A palavra secreta era: '{palavra_secreta}'")