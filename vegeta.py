def area_quadrado(lado):
    return lado * lado

def area_retangulo(base, altura):
    return base * altura

def main():
    lado = float(input("Digite o lado do quadrado: "))
    area1 = area_quadrado(lado)
    print(f"A área do quadrado é: {area1:.2f}")
    
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area2 = area_retangulo(base, altura)
    print(f"A área do retângulo é: {area2:.2f}")

main()
