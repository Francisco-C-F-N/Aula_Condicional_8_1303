
T1 = int(input("Digite o primeiro lado do triangulo "))

T2 = int(input("Digite o segundo lado do triangulo "))

T3 = int(input("Digite o terceiro lado do triangulo "))


if T1 == T2 == T3:
    print("Seu Triangulo é Equilatero")

elif T1 == T2 != T3:
    print("Seu triangulo é Isósceles")

elif T1 != T2 != T3:
    print("Seu triangulo é Escaleno")


    2