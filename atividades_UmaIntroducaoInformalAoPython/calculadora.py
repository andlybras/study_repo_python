import functools
import operator

def calculadora():

    historico = []

    while True:
        print("\n" + "-"*10 + " Calculadora " + "-"*10)
        print("\nEscolha uma operação: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Ver Histórico")
        print("\n0 - Sair")
        escolha = input("\nOpção: ")

        if escolha == "0":
            print("Calculadora encerrada.")
            break
        
        if escolha == "5":
            print("\n--- Histórico de Cálculos ---")
            if not historico:
                print("Nenhum cálculo foi realizado ainda.")
            else:
                for item in historico:
                    print(item)
            continue

        if escolha not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        numeros = []
        while True:
            try:
                if len(numeros) < 2:
                    prompt = f"Digite o {len(numeros) + 1}º número: "
                else:
                    prompt = "Digite o próximo número (ou '=' para calcular): "
                
                entrada = input(prompt).strip()

                if entrada.lower() == '=' and len(numeros) >= 2:
                    break
                
                numero = float(entrada)
                numeros.append(numero)

            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou '='.")
        
        resultado = 0
        operacao_str = ""

        if escolha == "1":
            resultado = sum(numeros)
            operacao_str = " + ".join(map(str, numeros))

        elif escolha == "2":
            resultado = functools.reduce(operator.sub, numeros)
            operacao_str = " - ".join(map(str, numeros))

        elif escolha == "3":
            resultado = functools.reduce(operator.mul, numeros)
            operacao_str = " * ".join(map(str, numeros))

        elif escolha == "4":
            try:
                resultado = functools.reduce(operator.truediv, numeros)
                operacao_str = " / ".join(map(str, numeros))
            except ZeroDivisionError:
                print("\nErro: Divisão por zero não é permitida.")
                continue

        historico_item = f"{operacao_str} = {resultado:.2f}"
        historico.append(historico_item)
        print(f"\nResultado: {historico_item}")