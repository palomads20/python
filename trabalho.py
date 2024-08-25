print("  -  Bem-vindos a loja da Paloma Mateus da Silva  - ")
print("             --Cárdapio--          ")

print("Tamanho",end=" | "), print("Bife acebolado (BA)",end=" | "), print("Filé de Frango (FF)")
print("P      ",end=" | "), print ("R$ 16,00           ",end=" | "), print("R$ 15,00          ")
print("M      ",end=" | "), print ("R$ 18,00           ",end=" | "), print("R$ 17,00           ")
print("G      ",end=" | "), print ("R$ 22,00           ",end=" | "), print("R$ 21,00           ")


valor=0
repetir= 'S'
total = 0

#começo da estrutura de repetição
while repetir == "S":
    sabor = input("Informe o sabor desejado (BA/FF): ").upper ()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        continue #continuar repetindo o input até ser inserido um valor valido 

    
    tamanho = input("Informe o tamanho desejado (P/M/G): ").upper ()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")

        continue #continuar repetindo o input até ser inserido um valor valido 

    if (sabor=="BA"):
     if (tamanho == "P"):
      valor = 16

     elif (tamanho=="M"):
      valor = 18

     elif (tamanho == "G"):
      valor = 22
     print(f"Você pediu um Bife Acebolado no valor de: R$ {valor}")

    elif (sabor == "FF"):
      if (tamanho == "P"):
       valor = 15

      elif (tamanho == "M"):
       valor= 17

      elif (tamanho == "G"):
       valor = 21
      print(f"Você pediu um Filé de Frango no valor de: R$ {valor}")

    total += valor
    repetir=input("Deseja mais alguma coisa?").upper ()
    if repetir== 'S':
     continue
    else:
      break #Quebrar a repetição
  
print (f"O valor total a ser pago é de: R$ {total}")