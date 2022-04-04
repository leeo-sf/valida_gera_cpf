from random import randint


numero = str(randint(100000000, 999999999))
novo_cpf = numero
total = 0 
reverso = 10 

for indice in range(19):
    if indice > 8: 
        indice -= 9  
        
    total += int(novo_cpf[indice]) * reverso 

    reverso -= 1 
    if reverso < 2:  
        reverso = 11  
        d = 11 - (total % 11)

        if d > 9: 
            d = 0  
            
        novo_cpf += str(d) 
        total = 0 

print(novo_cpf)
