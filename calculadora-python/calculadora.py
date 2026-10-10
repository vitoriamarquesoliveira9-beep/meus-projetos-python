print("=== Minha Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha uma operação: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "1":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "2":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "3":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Opção inválida. Escolha de 1 a 4.")