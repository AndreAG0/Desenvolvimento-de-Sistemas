''' 
Andre Galdino Arruda
RA : 1700619
'''
n = []
def subs(var):
    for x in range(0,20):
        if var[x] <= 0:
            var[x] = 0
        elif var[x] > 10:
            var[x] = 1
        else:
            var[x] = 2

for x in range (0,20):
    n.append(int(input("Digite um numero : ")))

subs(n)

for x in range(0,20):
    print(n[x])
