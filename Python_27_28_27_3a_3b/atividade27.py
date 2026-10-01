#27.	Receba o número de voltas, a extensão do circuito (em metros) 
#e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def velocidade(v, m, d:int):
    Km: float = 0.0
    horas: float = 0.0
    Vmedia: float = 0.0
    Km = (v*m)/1000
    horas = (d/60)
    Vmedia = (Km/horas)
    return Vmedia

def main():
    voltas = int(input("Qual é o número de voltas? "))
    extM = int(input("Qual é o tamanho do circuito (em metros)? "))
    duracao = int(input("Qual é o tempo de duração (minutos)? "))
    velocidadeM = velocidade(voltas, extM, duracao)
    print("A velocidade média é: ", velocidadeM, "km/h")

if (__name__ == '__main__'):
    main()