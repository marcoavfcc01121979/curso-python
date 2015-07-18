class Valores(object):
    
    def converter(self,real,dolar):
        convertido = real / dolar
        print("Valor convertido de real para dolar e ", convertido)

s = Valores()
real = float(input("entre com o valor em real para ser convertido em dolares "))
dolar = float(input("entre com os valor atual da moeda americana "))
s.converter(real,dolar)

        
