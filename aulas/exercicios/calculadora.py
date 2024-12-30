'''calculadora com while'''

# continuar = 1
# soma = calculadora + outro_number
# mult = calculadora * outro_number
# divi = calculadora / outro_number
# porc = calculadora / 100 * outro_number
#adicionar numero fracionario

#e tentar formatar no final por exe: se for numero inteiro e for 1.000 eu não quero 10.0 apenas para numeros fracionarios
#e colocar no final um ex: 10.0%

def add (calc1, calc2):    
    return int(calc1 + calc2)

def multiply (calc1, calc2):
    return int(calc1 * calc2)

def subtract (calc1, calc2):
    return int(calc1 - calc2)

def percentage (calc1, calc2):
    return float(calc1 / 100 * calc2)


operations  = {
    '+': add,
    '*':multiply,      
    '-':subtract,
    '%':percentage
}

while True:
    command = input ("enter operetion (+, *, -, %  'q' to quit)").lower()
    
    if command == 'q':
        print('OFF')
        break

    if command in operations:
        try:
            numb_1 = float(input('Enter first number: '))
            numb_2 = float(input('Enter second number: '))
            result = operations[command](numb_1, numb_2)

            if command == '%':
                print(f'{result:,.2f}%')
                
            elif isinstance(result, int):
                
                print(f'{result:,}') 
            
            else:
                print(f'{result:,.2f}') 
                
        except:
            print('Invalid input. Please enter numbers only')
            
    else:
        print("invalid operetions") 
    

   


            
            

     



    
  