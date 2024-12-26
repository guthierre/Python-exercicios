time = int(input('How time is:'))
good_morning  =  time in range (0, 12)

good_aftenoon = time in range(12, 18)

goood_night = time in range( 18, 24)

#time in range(18, 24)

    
if  good_morning :
    print('Good morning')
    
elif good_aftenoon :
    print('Good afternoon')
    
elif goood_night:
    print('Boa noite')

else:
    print('Olá, está tudo bem?')
    

