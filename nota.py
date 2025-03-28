while True:
    n1 = float(input('Digite sua nota do primeiro bimestre ?'))
    if n1 <=10 and n1 >=0:
        break
        


while True:
    n2 = float(input('Digite sua nota do segundo bimestre ?'))
    if n2 <=10 and n2 >=0:
        break
        

while True:
    n3 = float(input('Digite sua nota do terceiro bimestre ?'))
    if n3 <=10 and n3 >=0:
        break
        

while True:
    n4 = float(input('Digite sua nota do quarto bimestre ?'))
    if n4 <=10 and n4 >=0:
        break
        



mediafinal = (n1 + n2 + n3 + n4) / 4


print ("sua media foi " , mediafinal )

if (mediafinal >= 5):
    print("Voce foi APROVADO")

elif (mediafinal >= 3):
    print("voce esta em recuperacao")

else:
    print("voce foi REPROVADO")
    













