import random

def jokenpo():

    opcoes = ['Pedra', 'Papel', 'Tesoura']

    placar_computador = 0
    placar_usuario = 0

    while True:
        print("\n" + "~"*30 + " Jokenpô " + "~"*30)
        jogada_computador = random.choice(opcoes)
        jogada_usuario = input("\nEscolha Pedra, Papel ou Tesoura: ").capitalize()

        if jogada_usuario not in opcoes:
            print("\nJogada inválida! Tente novamente.")
            continue

        elif jogada_usuario == jogada_computador:
            print(f"\nEmpate! Ambos escolheram {jogada_usuario}.")

        elif jogada_usuario == "Pedra" and jogada_computador == "Tesoura" or \
             jogada_usuario == "Papel" and jogada_computador == "Pedra" or \
             jogada_usuario == "Tesoura" and jogada_computador == "Papel":
            print(f"\nVocê venceu! {jogada_usuario} vence {jogada_computador}.")
            placar_usuario += 1

        else:
            print(f"\nVocê perdeu! {jogada_computador} vence {jogada_usuario}.")
            placar_computador += 1

        print(f"\nPlacar: Você {placar_usuario} x Computador {placar_computador}")
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()

        while True:
            if jogar_novamente == 's':
                break
            elif jogar_novamente == 'n':
                print("\nObrigado por jogar! Até a próxima.")
                return
            else:
                jogar_novamente = input("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não: ").lower()

if __name__ == "__main__":
    jokenpo()