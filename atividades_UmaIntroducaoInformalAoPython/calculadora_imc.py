def calculadora_imc():
    
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")