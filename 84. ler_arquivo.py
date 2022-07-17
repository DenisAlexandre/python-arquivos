"""
Leitura de arquivos

"""

#Abrir um arquivo

#Função Open: Recebe como parâmetro obrigatório o endereço em que se encontra o arquivo.

#Obs.: A Abertura padrão é do mmodo leitura (mode 'r' - read)

arquivo = open("lucros.txt")
print(arquivo)

#Ler um arquivo
print(arquivo.read())# Função Read realiza a leitura do arquivo
print("-------------------------------------------------------")
print(arquivo.read())

arq = arquivo.read()
print(type(arq))

#Obs.: Delimitando a quantidade de caracteres (avanços do cursor)
arquivo = open("lucros.txt")
print(arquivo.read(5))


#Fechar um arquivo
arquivo = open("lucros.txt")
print(arquivo.closed)
arquivo.close() #Finaliza a conexao entre o arquivo aberto e o PyCharm (streaming)
print(arquivo.closed)

#Modo pythônico de trabalhar com arquivos
with open('lucros.txt') as luc:
    print(luc.read())
