'''
Andre Galdino Arruda
RA: 1700619
'''

arquivo = open('texto.txt', 'w')
arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
arquivo.write("--------------------------------------------------------------\n")
arquivo.write("Nr.\tUsuário        \tEspaço utilizado\t% do uso\n\n")
arquivo.write("1       Alexandre       434,99 MB               16,85%\n")
arquivo.write("2       Anderson        1187,99 MB              46,02%\n")
arquivo.write("3       Antonio         117,73 MB               4,56%\n")
arquivo.write("4       Carlos          87,03 MB                3,37%\n")
arquivo.write("5       Cesar           0,94 MB                 0,04%\n")
arquivo.write("6       Rosemary        752,88 MB               29,16%\n")
arquivo.write("\nEspaço total ocupado: 2581,57 MB\n")

arquivo.write("Espaço médio ocupado: 430,26 MB\n")

arquivo.close()
