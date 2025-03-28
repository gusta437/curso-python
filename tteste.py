def pedirNota(frase):
    while True:
        nota = float(input(frase))
        if nota >= 0 and nota <= 10:
            break
    return nota



n1 = pedirNota("digite a nota do 1 bimestre")
n2 = pedirNota("digite a nota do 2 bimestre")
n3 = pedirNota("digite a nota do 3 bimestre")
n4 = pedirNota("digite a nota do 4 bimestre")



mediafinal = (n1 + n2 + n3 + n4) / 4


print ("sua media foi " , mediafinal )

if (mediafinal >= 5):
    print("Voce foi APROVADO")

elif (mediafinal >= 3):
    print("voce esta em recuperacao")

else:
    print("voce foi REPROVADO")
    




