palavra_secreta = 'parfum'
letras_certas = ''
tentativas = 0
tentativas_max = 5

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        
    # if letra_digitada.isdigit():
    #     print('Apenas letras')
        continue

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
    else:
        tentativas_max -= 1
        print(f'Tentativas restantes: {tentativas_max}')

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            print(letra_secreta, end='')
        else:
            print('*', end='')
    print()  

    if letra_digitada in palavra_secreta:
    
      
        if palavra_secreta == letras_certas: 
            print('Você venceu')  
            break

    if tentativas_max == tentativas:
        print('Você Perdeu :)')
        break
   