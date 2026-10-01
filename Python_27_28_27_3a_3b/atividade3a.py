#Fazer um algoritmo que tenha uma função que receba um valor inteiro como
#parâmetro e retorne seu fatorial. O main deve solicitar ao usuário um valor,
#chamar a função, receber a saída da função em uma variável e exibir o resultado.
def Fatorial(n: int):
    fatorial: int = 1
    
    if (n == 0 or n == 1):
        return 1
    for i in range(2, n + 1):
        fatorial = fatorial * i
    return fatorial


def main():
    num: int = 0
    num = int(input("Digite um número inteiro: "))
    
    if num < 0:
        print("Não existe fatorial de números negativos")
    else:
        res: int = Fatorial(num)
        print("O fatorial do número é: ", res)

if __name__ == '__main__':
    main()