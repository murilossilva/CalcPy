import math as m

print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
print('5 - Potenciação\n6 - Raiz quadrada\n7 - Raiz Cúbica\n8 - Logaritmo')
print('0 - Sair\n')
menu = int(input("Digite a operação desejada: "))
print('')

x = 1

#Função para realizar novamente o uso da calculadora#

def novamente(x):
    while x == 1:
        r = str(input('Gostaria de continuar?[s/n] '))
        if r in 'nN':
            print('Obrigado por confiar nos meus cálculos, volte logo!')
            return False
        if r in 'sS':
            return True
        else:
            print('Informe uma opção válida')

if menu == 0:
    print('Tudo bem, estarei te aguardando!')

while menu != 0:
    if menu not in range(0,9):
        print('Eiiiii! Essa opção não existe, tente novamente!\n')
        menu = int(input('Digite a operação desejada: '))
    #soma        
    if menu == 1:
        n = float(input('Digite o primeiro valor a ser somado: '))
        m = float(input('Digite o segundo valor a ser somado: '))
        print('O resultado de {} + {} = {}\n'.format(n, m, round(float(n) + float(m), 2)))
        if novamente(x) == False:
            break
    #subtração
    if menu == 2:
        n = float(input('Digite o primeiro valor a ser subtraído: '))
        m = float(input('Digite o segundo valor a ser subtraído: '))
        print('O resultado de {} - {} = {}\n'.format(n, m, round(float(n) - float(m), 2)))
        if novamente(x) == False:
            break
    #multiplicação    
    if menu == 3:
        n = float(input('Digite o primeiro valor a ser multiplicado: '))
        m = float(input('Digite o segundo valor a ser multiplicado: '))
        print('O resultado de {} * {} = {}\n'.format(n, m, round(float(n) * float(m), 2)))
        if novamente(x) == False:
            break
    #divisão    
    if menu == 4:
        n = float(input('Digite o dividendo: '))
        m = float(input('Digite o divisor: '))
        if m != 0:
            print('O resultado de {} / {} = {}\n'.format(n, m, round(float(n) / float(m), 2)))
        #regra para o divisor diferente de 0
        else:
            print('O divisor não pode ser nulo, tente novamente!')
        if novamente(x) == False:
            break
    #potenciação    
    if menu == 5:
        n = float(input('Digite o valor da base: '))
        m = float(input('Digite o valor do expoente: '))
        print('O resultado de {}^{} = {}\n'.format(n, m, round(float(n) ** float(m), 2)))
        if novamente(x) == False:
            break
    #raiz quadrada
    if menu == 6:
        n = float(input('Digite o valor do radicando: '))
        print('A raiz quadrada de {} é = {}\n'.format(n, float(m.sqrt(n))))
        if novamente(x) == False:
            break
    #raiz cúbica
    if menu == 7:
        n = float(input('Digite o valor do radicando: '))
        print('A raiz quadrada de {} é = {}\n'.format(n, float(n) ** (1/3)))
        if novamente(x) == False:
            break
    #logaritmo
    if menu == 8:
        n = float(input('Digite o valor do logaritmando: '))
        base = float(input('Digite o valor da base: '))
        print('O resultado do logaritmo de {} na base {} = {}\n'.format(n, base, (m.log(n)/m.log(base))))
