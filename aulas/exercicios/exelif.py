valor1= int(input('Digite um valor:'))
valor2= int(input('Digite outro valor:'))



if valor1 > valor2:
    print('O Valor1:{}\n é maior que o valor2:{}'.format(valor1, valor2))
elif valor2 > valor1:
    print('Valor2:{}\n é maior que o valor1:{}'.format(valor2,valor1))
else:
    print('Ambos valores são iguais')