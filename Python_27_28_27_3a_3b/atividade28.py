#28.	Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que: 
# Venda Mensal	  Preço Atual	Preço Novo
# < 500	             < 30	      +10%
#>= 500 e < 1000	>= 30 e < 80  +15%
#>= 1000	        >= 80	      -5%
#Obs.: para outras condições, preço novo será igual ao preço atual.
def preçoN(m:float, p:float):
    preconovo: float = 0.00

    if(m < 500 and p < 30):
        preconovo = (p * 1.10)
    elif(m >= 500 and m < 1000 and p >= 30 and p < 80):
        preconovo = (p * 1.15)
    elif(m >= 1000 and p >= 80):
        preconovo = (p * 0.95)
    else:
        preconovo = p
    return preconovo

def main():
    mediaM: float = 0.00
    PAtual: float = 0.00
    mediaM = float(input("Qual é o média mensal? "))
    PAtual = float(input("Qual é o preço atual? "))
    Pnovo = preçoN(mediaM, PAtual)
    Pnovo = round(Pnovo, 2)
    print("O novo preço é: R$", Pnovo)

if (__name__ == '__main__'):
    main()