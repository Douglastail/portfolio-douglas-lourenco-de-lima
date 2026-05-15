def simulador_evacuacao():

    locais = ["Quarto", "Cozinha", "Sala", "Porta", "Portão"]

    posicao = 0
    energia = 10

    print("INICIANDO EVACUAÇÃO...\n")

    while energia > 0:

        print(f"Você está em: {locais[posicao]}")

        if locais[posicao] == "Portão":
            print("Você saiu com sucesso!")
            break

        escolha = input("Digite D para direita ou E para esquerda: ")

        if escolha.upper() == "D":

            if posicao < len(locais) - 1:
                posicao += 1

        elif escolha.upper() == "E":

            if posicao > 0:
                posicao -= 1

        else:
            print("Comando inválido!")

        energia -= 1

        print(f"Energia restante: {energia}\n")


simulador_evacuacao()
