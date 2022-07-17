"""
1 - Criar um arquivo de texto, inserir o lucro mensal de uma startup 
entre os meses de janeiro e maio, informando o mês e o valor, através 
da entrada do usuário. Após isso, ler o arquivo e imprimir o mês de 
maior lucro.
"""

# 1
with open('LucrosEmpresa.txt', 'w') as LE: #Abre o arquivo em modo de escrita
    while True:
        mes = input('Mês: ')
        if mes == 'sair':
            break
        else:
            LE.write(f'{mes}: ') #Escreve o mês no arquivo
            LE.write(input('Lucro: '))
            LE.write('\n')

relatorio = {}

with open('LucrosEmpresa.txt') as LE:
    for linha in LE:
        relatorio[linha[0:3]] = int(linha[5:]) 
        #A chave do dicionário é o mês (da posição 0 até
        # a 3), e o valor é o lucro (da posição 5 até o final da linha).
print(relatorio)
maiorLucro = 0
mesMaiorLucro = ''

for mes, lucro in relatorio.items():
    if lucro > maiorLucro:
        maiorLucro = lucro
        mesMaiorLucro = mes
        
print(f"Mês com maior lucro: {mesMaiorLucro} com R$ {maiorLucro}")