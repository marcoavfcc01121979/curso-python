class Capacidade(object):
    def maxima(self, tamanho, capEmMetrosQuadrados = 1.5):
        capacidade = tamanho / capEmMetrosQuadrados
        print("A Capacidade de alunos na sala e ", capacidade)

c = Capacidade()
tamanho = float(input("entre com o tamanho da sala em metros quadrados "))
c.maxima(tamanho)
        
