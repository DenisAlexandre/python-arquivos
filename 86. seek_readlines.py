"""
Seek e ReadLine

"""
print("teste")
arquivo = open('lucros.txt')
print(arquivo.read())

print(arquivo.read())

arquivo.seek(0)#Move para o inicio do arquivo
print(arquivo.read())
arquivo.close()

arquivo = open("lucros.txt")
linha = arquivo.readline()
print(linha)

#readlines retorna uma lista de linhas
