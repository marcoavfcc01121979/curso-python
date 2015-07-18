class Altura(object):

    def pes(self,altura,pes= 30 ):
        convercao = (altura * 100) / pes
        print("A Altura em pes e ", convercao)

a = Altura()
altura = float(input("Entre com o tamanho de Sua Altura "))
a.pes(altura)
        
