from random import randint
print("bem vindo")
numero_sorteado= randint(1,100)
print(numero_sorteado)
novo_jogo = True
while novo_jogo !=False:
    numero_sorteado = randint(1,100)
    contador = 1
    while True:
        chute = int(input("Chute um numero:"))
        if chute == numero_sorteado:
            print ("Parabéns, vocêw é foda.")
            break
        else:
            print("also if chute > numero_sorteado else "Baixo")
                  copntador += 1
                  print("Fim de jogo")
                  print("Númerro sorteado:" +str(numero_sorteado))
                  print("Numero chutado:" + str(chute))
                  print("numero de tentativas:"+ str(contador))
                  novo_jogo = int(input("Jogar novamente")
