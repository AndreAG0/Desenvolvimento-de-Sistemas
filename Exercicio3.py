valor = int(input("Digite um valor : "))
if valor < 0:
    print(valor * -1)
elif valor > 10:
    valor2 = int(input("Digite um segundo valor : "))
    print ("A diferença entre os valores é :", valor - valor2)
else:
    print(valor / 5)
