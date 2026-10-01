#Modificar o exercício 3a e criar uma função que receba 2 parâmetros inteiros e
#retorne a divisão do primeiro pelo segundo. O main deve solicitar o valor de N e
#usar as funções para calcular e exibir 1 + 1/1! + 1/2! + ... + 1/N!
def Fatorial(n: int):
    fatorial: int = 1
    
    if (n == 0 or n == 1):
        return 1
    for i in range(2, n + 1):
        fatorial = fatorial * i
    return fatorial

def Divisao(dividendo: int, divisor: int):
    if divisor == 0:
        return 0.0
    return dividendo / divisor

def main():
    n: int = 0 
    n = int(input("Digite o valor de N: "))
    
    if n < 0:
        print("Não existe fatorial de números negativos")
    else:
        soma_sequencia: float = 1.0
        
        for i in range(1, n + 1):
            fat_atual = Fatorial(i)        
            termo_atual = Divisao(1, fat_atual) 
            soma_sequencia = soma_sequencia + termo_atual
            
        print("O resultado da sequência é: ", soma_sequencia)

if __name__ == '__main__':
    main()