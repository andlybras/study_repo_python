import random

def advinhe_numero_secreto(inicio_intervalo, fim_intervalo):

    numero_secreto = random.randint(inicio_intervalo, fim_intervalo)
    tentativas = 0

    while True:

        try:
            palpite = int(input("\nDê o seu palpite: "))
            tentativas += 1

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
            continue
        
        if palpite == numero_secreto:
            print("\nParabéns! Você acertou!")
            print(f"\nVocê precisou de {tentativas} tentativas para acertar o número secreto")
            break

        elif palpite < numero_secreto:
            print("\nPalpite errado! Tente um número maior")

        else:
            print("\nPalpite errado! Tente um número menor")

print("\n" + "~"*30 + " Advinhe o Número Secreto " + "~"*30)
print("\nDigite 1 para definir o intervalo de números para adivinhar ou 2 para jogar com o intervalo padrão de 1 a 100")

while True:

    acao_inicial = int(input("Ação Inicial: "))

    try:

        if acao_inicial == 1:
            inicio_intervalo = int(input("Digite o início do intervalo: "))
            fim_intervalo = int(input("Digite o fim do intervalo: "))
            advinhe_numero_secreto(inicio_intervalo, fim_intervalo)

            break

        elif acao_inicial == 2:
            inicio_intervalo = 1
            fim_intervalo = 100
            advinhe_numero_secreto(inicio_intervalo, fim_intervalo)
            
            break
        
        else:
            print("\nAção Inválida! Tente 1 ou 2.")

    except ValueError:
        print("\nAção Inválida! Tente 1 ou 2.")