from calculadora_imc import calculadora_imc
from conversor_temperatura import conversor_temperatura
from juros_compostos import juros_compostos
from inversor_palavras import inversor_de_palavras
from contador_vogais import contator_vogais
from gerador_acronimos import gerador_acronimos

def atividades():

    while True:
        print("#"*60)
        print("\nQual atividade você deseja realizar? ")
        print("\n1 - Calcular IMC")
        print("2 - Converter temperatura")
        print("3 - Calcular juros compostos")
        print("4 - Inverter palavra")
        print("5 - Contar vogais")
        print("6 - Gerar acrônimo")
        escolha = input("\nDigite o número da atividade desejada: ")

        try:
            if escolha == "1":
                calculadora_imc()
            elif escolha == "2":
                conversor_temperatura()
            elif escolha == "3":
                juros_compostos()
            elif escolha == "4":
                inversor_de_palavras()
            elif escolha == "5":
                contator_vogais()
            elif escolha == "6":
                gerador_acronimos()
            else:
                print("Opção inválida. Tente novamente.")
        except:
            print("Opção inválida. Tente novamente.")

atividades()