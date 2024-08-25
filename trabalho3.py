print (" Bem vindos a loja de camisetas da Paloma Mateus da Silva")

print ("MCS-Camiseta Manga Curta Simples ")
print ("MLS-Camiseta Manga Longa Simples ")
print ("MCE-Camiseta Manga Curta Com Estampa ")
print ("MLE-Camiseta Manga Longa Com Estampa")

def escolha_modelo (): #escolha_modelo é o nome do lugar onde as informações estão salvas (função)
   while True: 
    modelo=input("Entre com o modelo desejado (MCS,MLS,MLE,MCE)  ")
    if modelo == "MCS": 
     return 1.80     #return é o valor que irá retornar lá no main
    elif modelo == "MLS":
     return 2.10
    elif modelo == "MLE":
     return 3.20
    elif modelo == "MCE":
      return 2.90
    else:
     print("Escolha inválida, entre com o modelo novamente")
     continue
     
    

def num_camisetas ():
  while True:
   try:
    numero=float(input("Entre com o número de camisetas  "))

    if numero >= 2000 and numero < 20000:
     desconto = 0.12
    

    elif numero >= 200 and numero <2000:
     desconto = 0.07
    

    elif numero >= 20 and numero <200:
     desconto = 0.05

    elif numero < 20:
     desconto = 0
    
    else:
      print("Não aceitamos tantas camisetas de uma vez. Informe o número de camisetas novamente.")
      continue

   except ValueError:
     print("Por favor, entre com o número de camisetas novamente")
     continue
   return desconto,numero
   
 
  
def frete():
 while True:
   
  frete1= int(input("Escolha o tipo de frete (0-Retirar na fábrica /1 - Transportadora/2- SEDEX)  "))
  if frete1 == 1:
   return 100
  elif frete1 == 2:
   return 200
  elif frete1 == 0:
   return 0
  else:
   print ("Invalido")

#principal

modelo= escolha_modelo()
desconto,numero= num_camisetas()
frete1= frete()

total1= modelo*numero
total2= total1*(1-desconto)+frete1
total3=numero*(1-desconto)

print(f'Valor total:{total2}' f"  (Modelo:{modelo} * Número de camisetas(Com desconto já aplicado):{total3} + Frete: {frete1}.00)")