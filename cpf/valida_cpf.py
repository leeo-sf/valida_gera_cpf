def valida_cpf(cpf):
    novo_cpf = cpf[:9]  # Pega os caracteres do 0 ao 9 do cpf - Eliminando os dois ultimos.
    total = 0  # Armazena o resultado da multiplicação do cpf
    reverso = 10  # Contador reverso

    for indice in range(19):
        if indice > 8:  # Se o indice for maior que 8
            indice -= 9  # Indice irá voltar para o primeiro digito do cpf e ir áte o 9
        
        total += int(novo_cpf[indice]) * reverso  # Multiplica cada número do cpf do 10 de forma decrescente

        reverso -= 1  # A cada volta é subtraído 1 a varável reverso
        if reverso < 2:  # Se reverso for menor que 2
            reverso = 11  # Reverso será igual a 11
            d = 11 - (total % 11)

            if d > 9:  # Se o calculo de "d" for mais que 9
                d = 0  # "d" se torna 0
            
            novo_cpf += str(d)  # Adiciona o "d" no cpf como digito (dois ultimos números do cpf)
            total = 0  # A variável total volta a ser 0
    
    # Evita sequências. EX. 11111111111, 00000000000. ...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(novo_cpf)
    
    if not novo_cpf == cpf and sequencia:  # Se o novo_cpf não for igual ao cpf digitado - O usuário pode ter digitado algo errado
        return False  # CPF inválido
    else:  # Senão
        return True  # CPF válido


def formata_cpf(cpf):

    if "-" in cpf:
        cpf = cpf.replace("-", "")
    
    if "." in cpf:
        cpf = cpf.replace(".", "")
    
    return cpf

