'''CONSTANTE= "VARIVEIS" que não vão mudar
muitas condições no mesmo if(ruim)

    <- contagem de complexidade(ruim)
    
'''

velocidade = 71 #velocidade atual do carro
local_carro = 101 #local em que o carro está na estrada

LIMITE_RADAR1 = 60 #velocidade maxima no radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGER = 1 # A Distancia onde o radar pega.
contagem_multa = velocidade + LIMITE_RADAR1 
multa = contagem_multa /100 * 100
carro_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and  local_carro <= (LOCAL_1 + RADAR_RANGER)
multa_normal = velocidade > LIMITE_RADAR1 and velocidade <= LIMITE_RADAR1 + 10
multa_perigosa = local_carro>=(LOCAL_1 - LIMITE_RADAR1) and velocidade > LIMITE_RADAR1 + 10
  
if carro_radar1:

    if multa_normal:  
        
     print(f'O Carro passou {velocidade} KM')    
     print(f'A Multa normal de R${multa:.2f}')

    elif multa_perigosa:
     print(f'A sua multa foi de alto risco {multa * 5:.2f}')

else:
    print(f'não tem multas pendentes')
'''
'''