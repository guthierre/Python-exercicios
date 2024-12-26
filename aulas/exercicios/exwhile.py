
#       012345678
name = 'Guthierre' #iteráveis *G*U*T*


fake_name = ''

number_name = 0 

while number_name < len(name):
    
    fake_name += name[number_name] + '*'
    
    number_name += 1
    
    print(fake_name)