'''
Exercícios:
1) Teste se um arquivo chamado livros.txt não exista pela abertura x, caso o
arquivo já exista abra como w+, utilize Try/Except nessa manipulação. Imprima
na tela qual foi o modo de abertura, escreva no bloco o nome dos três melhores
livros que você já leu (um em cada linha) adicionando ao arquivo, feche-o. Abrao novamente e adicione mais um livro ao final do arquivo sem apaga-lo, por fim,
leia a versão final.
Resposta:
1)
'''

try: #Tente abertura no modo x
    with open('livros.txt', 'x') as arq:
        print("Abrimos o arquivo no modo 'x'")
        arq.write('Geracao de Valor') #Escreve o texto no arquivo
        arq.write('\nOs Segredos da Mente Milionaria')
        arq.write('\nO poder do Habito')
except FileExistsError: #Caso ocorre o erro FileExistsError faça:
    with open('livros.txt','w+') as arq: #Abre no modo w+
        print("Abrimos o arquivo no modo 'w+'")
        arq.write('Geracao de Valor')
        arq.write('\nOs Segredos da Mente Milionaria')
        arq.write('\nO poder do Habito')
        
with open('livros.txt','a+') as arq: #Abre o arquivo sem apagá-lo e
    #adiciona ao final o livro
    arq.write('\nSherlock Holmes')
    arq.seek(0)
    print(arq.read())
