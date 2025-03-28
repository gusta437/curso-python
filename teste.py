def obter_preco():
    while True:
        try:
            preco = float(input("Digite o preço do produto: R$ "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
            else:
                return preco
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

def calcular_media(preco1, preco2, preco3):
    return (preco1 + preco2 + preco3) / 3

# Solicitar os preços
print("Informe os preços de 3 produtos:")
preco1 = obter_preco()
preco2 = obter_preco()
preco3 = obter_preco()

# Calcular a média
media = calcular_media(preco1, preco2, preco3)

# Exibir o resultado
print(f"\nA média dos preços é: R$ {media:.2f}")
