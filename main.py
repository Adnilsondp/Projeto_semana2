def soma_tres(num1, num2, num3):
    """Função que soma três números."""
    return num1 + num2 + num3

if __name__ == "__main__":
    # Pede três números para o usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    # Faz a soma usando a função
    resultado = soma_tres(num1, num2, num3)

    # Mostra o resultado
    print(f"A soma de {num1} + {num2} + {num3} é {resultado}")