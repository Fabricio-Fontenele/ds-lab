import os

operations = {
    "+": "soma",
    "-": "subtração",
    "/": "divisão",
    "x": "multiplicação",
    "^": "exponenciação",
}

while True:
    os.system("clear")

    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1

    op = int(input("Escolha a operação que deseja realizar "))
    opToString = list(operations.values())[op]
    print(f"{opToString} escolhida")
    try:
        n1 = float(input("Digite o primeiro valor\n"))
        n2 = float(input("Digite o segundo valor\n"))
        if op == 0:
            print(n1 + n2)
        elif op == 1:
            print(n1 - n2)
        elif op == 2:
            print(n1 / n2)
        elif op == 3:
            print(n1 * n2)
        elif op == 4:
            print(n1**n2)
    except ValueError:
        print("Valor não aceito")
    except ZeroDivisionError:
        print("Erro: Divisão por zero")

    should_continue = input("Quer continuar [S/N]? ").strip().upper()

    if should_continue == "N":
        break
    elif should_continue != "S":
        print("Resposta inválida. Continuando...")
