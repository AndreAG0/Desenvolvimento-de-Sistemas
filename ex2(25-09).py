Satan = 1
x = 0
p = []
t = 0
while Satan == 1:
    while x == 0:
        y = float(input("Digite o preço do produto : "))
        p.append(y)
        t = t + y
        if y == 0:
            x = 1
    arq = open("recibo.txt" , "w")
    arq.write("Lojas Tabajara \n")
    for l in range(0,len(p)-1):
         arq.write("Produto %i : R$ %i \n" % (l, p[l]))
    arq.write("Total : R$ %i \n" % (t))
    d = float(input("Digite o dinheiro recebido :"))
    arq.write("Dinheiro : R$ %i \n"%(d))
    arq.write("Troco : R$ %i \n"%(d-t))
    arq.close()

input()
