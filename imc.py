sair = "Não" 
while sair == "Não":
    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))

    imc = peso / (altura*altura)

    print("seu IMC é ", imc )


    sair = input("Deseja sair? sim/nao: ")