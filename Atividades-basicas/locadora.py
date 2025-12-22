import os

carros_disponiveis = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]

carros_alugados = []


def print_formatted_list(cars_list):
    for i, (car, price) in enumerate(cars_list):
        print(f"[{i}] {car} - R$ {price} /dia")


while True:
    os.system("clear")

    print("=" * 5)
    print("Bem Vindo à locadora de carros!")
    print("=" * 5)
    print("O que deseja fazer ?")
    print("0 - mostrar portifolio | 1 - Alugar um carro | 2 - Devolver um carro")

    escolha = int(input())
    if escolha == 0:
        os.system("clear")
        print("Carros disponíveis para aluguel:")
        print_formatted_list(carros_disponiveis)
    elif escolha == 1:
        os.system("clear")
        print("Carros disponíveis para aluguel:")
        print_formatted_list(carros_disponiveis)
        indice = int(input("Digite o índice do carro que deseja alugar: "))
        dias = int(input("Por quantos dias deseja alugar? "))
        if 0 <= indice < len(carros_disponiveis):
            aluguel = carros_disponiveis[indice]
            total = aluguel[1] * dias
            print(f"O total do aluguel por {dias} dias é R$ {total}")
            confirmar = input("Deseja confirmar o aluguel? [S/N] ").strip().upper()
            if confirmar != "S":
                print("Aluguel cancelado.")
                continue
            carro_selecionado = carros_disponiveis[indice]
            carros_disponiveis.remove(carro_selecionado)
            carros_alugados.append(carro_selecionado)
            print(f"Você alugou o carro: {carro_selecionado[0]}")
        else:
            print("Índice inválido.")
    elif escolha == 2:
        os.system("clear")
        if not carros_alugados:
            print("Nenhum carro alugado no momento.")
        else:
            print("Carros alugados:")
            print_formatted_list(carros_alugados)
            indice = int(input("Digite o índice do carro que deseja devolver: "))
            if 0 <= indice < len(carros_alugados):
                carro_devolvido = carros_alugados.pop(indice)
                carros_disponiveis.append(carro_devolvido)
                print("Carro devolvido com sucesso.")
            else:
                print("Índice inválido.")

    continuar = input("Quer continuar [S/N]? ").strip().upper()
    if continuar == "N":
        break
    elif continuar != "S":
        print("Resposta inválida. Continuando...")
