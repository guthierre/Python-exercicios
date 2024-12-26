'''
iNTRODUÇÃO AO TRY/EXCEPT

TRY -> TENTAR EXECUTAR O CODIGO
AXCEPT - > OCORREU ALGUM ERRO AO TENTAR EXECUTAR

sempre que usuario me mandar algo eu preciso tratar o valor do input

'''


numero_str = input('Vou dobrar o numero que você digitar: ')

#print (numero_str.isdigit())

#FAIL FAST
try:
    print('STR:', numero_str)  
    print('*'*10)
    numero_float = float(numero_str)
    print(f'O Dobro de :{numero_str} é :{numero_float*2}')
    print('*'*10)
    print('FLOAT: ', numero_float)
    print('*'*10)
    

    

except:
    print('Isso não é um numero')



#IF CHECA UMA CONDIÇÃO E MUDA O FLUXO
#if numero_str.isdigit():
 #   print(f'O Dobro: {numero_str * 2:.2f}')

#else:
#    print('Isso não é um numero')