from calculadora_imc import calculadora_imc
from conversor_temperatura import conversor_temperatura
from juros_compostos import juros_compostos

def atividades():

    while True:
        print("#"*60)
        print("\nQual atividade você deseja realizar? ")
        print("\n1 - Calcular IMC")
        print("2 - Converter temperatura")
        print("3 - Calcular juros compostos")
        escolha = input("\nDigite o número da atividade desejada: ")

        try:
            if escolha == "1":
                calculadora_imc()
            elif escolha == "2":
                conversor_temperatura()
            elif escolha == "3":
                juros_compostos()
            else:
                print("Opção inválida. Tente novamente.")
        except:
            print("Opção inválida. Tente novamente.")

atividades()