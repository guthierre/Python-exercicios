
texto = 'Guthi'#iteravel
iterator = iter(texto) #interador]

# for letra in texto

while True:
    
    try:
        letra = next(iterator)
      
        print(letra)
    
    except StopIteration:  
        break