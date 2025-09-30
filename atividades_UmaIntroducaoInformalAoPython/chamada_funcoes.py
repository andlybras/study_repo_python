from calculadora_imc import calculadora_imc
from conversor_temperatura import conversor_temperatura

def atividades():

    while True:
        print("#"*60)
        print("\nQual atividade você deseja realizar? ")
        print("\n1 - Calcular IMC")
        print("2 - Converter temperatura")
        escolha = input("\nDigite o número da atividade desejada: ")

        try:
            if escolha == "1":
                calculadora_imc()
            elif escolha == "2":
                conversor_temperatura()
        except:
            print("Opção inválida. Tente novamente.")

atividades()