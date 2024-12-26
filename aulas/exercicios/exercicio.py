nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if nome and idade :
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido fica: {nome[-1:-10:-1]}')     
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A Primeira letra do seu nome é:{nome[0]}')
    print(f'A Ultima letra do seu nome é {nome[-1]}')
    print(f'Seu nome contém ou não espaço?{' ' in nome}')
else:
    print('Invalido!')