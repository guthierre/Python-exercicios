'''
repeat
while
executação uma condição enquanto for verdadeira
infinite loop while the code no have ends
'''
condition = True
while condition:
    name = input('Whats your name?')
    print(f'Your name is {name}')  
    if name == 'sair':
        break
    
print('Acabou')
        