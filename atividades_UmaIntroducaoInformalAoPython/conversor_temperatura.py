def conversor_temperatura():

    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    temperatura_fahrenheit = (temperatura * 9/5) + 32
    
    print(f"\n{temperatura} graus Celsius equivalem a {temperatura_fahrenheit} graus Fahrenheit.")