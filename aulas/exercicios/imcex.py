altura = float(input('qual sua altura?'))
peso = float(input('qual seu peso?'))
imc= peso / (altura * altura)  
pesonor = 18.5 <= imc >= 24
pesoabai=   18 >= imc

print('O Seu peso ideal é:{:.2f}\n seu peso está normal: {}\n você está abaixo do peso {} '.format(imc,pesonor,pesoabai))