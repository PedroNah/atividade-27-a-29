#29.Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. 
# Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. 
# Demais tipos não serão considerados.

def calcularI(tipo: int, valor: float):
    valorC: float = 0.0
    
    if tipo == 1:
        valorC = valor * 1.03
        print("O valor corrigido na Poupança em 30 dias é: R$", valorC)
    elif tipo == 2:
        valorC = valor * 1.05
        print("O valor corrigido na Renda Fixa em 30 dias é: R$", valorC)
    else:
        print("Tipo de investimento inválido! Demais tipos não serão considerados")

def main():

    print("Opções: 1 = Poupança | 2 = Renda Fixa")
    tipoI: int = int(input("Qual é o tipo de investimento: "))
    valorI: float = float(input("Qual é o valor a ser investido: R$"))
    calcularI(tipoI, valorI)

if __name__ == '__main__':
    main()