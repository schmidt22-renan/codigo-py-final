import random

print("#########################")
print("#  jogo do calibre  aeatorio#")
print("#########################")

calibreSecreto= random.randrange(9,20,32,30,.40.45acp,.44,.50.,762,765,) 
totalTentativas = 0
pontos = 100
print("Qual niveis de dificuldade?  ")
print("(1) - facil (2) - medio (3) - dificil ")

nivel = int(input("Escolha um nivel"))

if(nivel == 1):
  print("banbi ")
  totaltentativas  = 25
elif (nivel == 2):
    print("fraco")
    totaltentaivas = 10
elif(nivel == 3):
    print("konan")
    totaltentativas = 5

for rodada in range (1, totalTentativas +1):
    print("tentativa {} de {}".format(rodada,totalTentativas) )
    chute_str = input("Digite um calibre entre 9 e 765: ")
    chute = int(chute_str)
     
    if(chute< 1 or chute >100):
       print("Numero invalido")
       continue
    
    acertou = chute == calibreSecreto
    maior = chute > calibreSecreto
    menor = chute < calibreSecreto

    if(acertou):
       print(f"Voce acertou e fez {pontos}! ")
       break
    else:
        if(maior):
           print("Vove errou! Seu chute foi maior que o numero secreto")
        elif(menor):
           print("Voce errou! Seu chute foi menor que o numero secreto")

           pontosPerdidos = abs( - chute)
           pontos = pontos - pontosPerdidos
           
    print("Fim da batalha! O numero " ,numeroSecreto)
    
    