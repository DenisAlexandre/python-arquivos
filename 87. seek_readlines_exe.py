"""
1 - Crie um arquivo com conteúdo aleatório. Em seguida, abra o arquivo, 
leia-o 3 vezes a partir dos caracteres 5, 9, 14. 
Por fim, feche o arquivo

"""
arq = open('Cores.txt')
#Mover o cursor para a 5º posição
arq.seek(5)
print(f'\n\n{arq.read()}')

#Mover o cursor para a 9º posição
arq.seek(9)
print(f'\n\n{arq.read()}')


#Mover o cursor para a 14º posição

arq.seek(14) #A quebra de linha conta para o seek
print(f'\n\n{arq.read()}')
arq.close()
