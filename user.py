from cpf.valida_cpf import valida_cpf, formata_cpf

while True:
    cpf = input("Digite seu CPF: ")
    cpf_format = formata_cpf(cpf)

    if len(cpf) < 11:
        print("O CPF não foi digitado por completo. Tente Novamente.")
        break

    if len(cpf) > 14:
        print("O CPF é composto por 14 caracteres contendo (- e ,). Você digitou mais de 14 caracteres. Tente Novamente.")
        break

    if not valida_cpf(cpf_format):
        print("\tCPF INFORMADO INVÁLIDO. TENTE NOVAMENTE")
        break
    else:
        print("\tCPF Informado Válido!")

        y_n = input("Deseja valida outro CPF? 'y' para yes ou 'n' para no: ").lower()

        if y_n == "y":
            continue

        elif y_n == "n":
            break

        elif not y_n == "y" or y_n == "n":
            print("Informação inválida. Tente novamente.")
            break
