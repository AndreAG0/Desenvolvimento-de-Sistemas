arquivo = open("arquivo1.txt", "w")

arquivo.write('Qualquer Coisa')

arquivo.close()
arquivo = open("arquivo1.txt", "r")

copia = arquivo.read()
arquivo.close()

arquivo2 = open("arquivo2.txt", "w")

arquivo2.write(copia)

arquivo2.close()
