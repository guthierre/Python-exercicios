# senha_salva ='123456'
# senha_digitada =''
# repeticoes = 0
# repeticoes_max = 5

# while senha_salva != senha_digitada:
    
#     senha_digitada = input (f'sua senha ({repeticoes}x)')
#     repeticoes += 1
    
#     if repeticoes >= repeticoes_max:
#         print('Você tentou demais')
#         break

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    
    print(letra, novo_texto)