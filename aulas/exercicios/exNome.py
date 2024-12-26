name = str(input('Whats your name?:'))
short_name =len(name) >= 1 and len(name)<= 4
normal_name = len(name) >= 5 and len(name) <= 6
long_name = len(name) >= 7


if short_name:
    print(f'its short name\n:{name}')
    
elif normal_name:
    print(f'Your name is normal\n:{name}')
    
elif long_name >= 7:
    print(f'is a big name\n:{name}')
    
else:
    print('Digite mais de uma letra',)