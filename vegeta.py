def area_quadrado(lado):
    return lado * lado

def main():
    lado = float(input("Digite o lado do quadrado: "))
    area = area_quadrado(lado)
    print(f"A área do quadrado é: {area:.2f}")

main()
