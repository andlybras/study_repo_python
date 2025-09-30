def calculadora_imc():
    
    peso = float(input("\nDigite seu peso em kg: "))
    altura = float(input("\nDigite sua altura em metros: "))

    imc = peso / (altura ** 2)

    print("")
    print(f"\nSeu IMC é: {imc:.2f}")