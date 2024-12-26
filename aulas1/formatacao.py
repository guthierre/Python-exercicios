'''
FORMATAÇÃO BASICA DE F-STRINGS

s - string
d - int
f - float
.<Numero de digitos> f
x ou X - hexadecimal
(carectere) (><^)(quantidade)
>esquerda
<direita
^ centro
sinal - + ou -
ex.: 0>-100,.1f
conversion flags-!r !s !a
'''
variavel = 'abc'
print (f'{variavel}')
print (f'{variavel: ^10}')
print (f'{variavel: <10}')
print (f'{variavel: >10}')
print (f'{1000.12149194148148184:.2f}')