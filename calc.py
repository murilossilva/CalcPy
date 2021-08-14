print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n')
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
            break
        if r in 'sS':
            return True

if menu == 0:
    print('Tudo bem, estarei te aguardando!')

while menu != 0:
    if menu not in range(0,5):
        print('Eiiiii! Essa opção não existe, tente novamente!\n')
        menu = int(input('Digite a operação desejada: '))
            
    if menu == 1:
        n = float(input('Digite o primeiro valor a ser somado: '))
        m = float(input('Digite o segundo valor a ser somado: '))
        print('O resultado de {} + {} = {}\n'.format(n, m, round(float(n) + float(m), 2)))
        if novamente(x) == False:
            break

    if menu == 2:
        n = float(input('Digite o primeiro valor a ser subtraído: '))
        m = float(input('Digite o segundo valor a ser subtraído: '))
        print('O resultado de {} - {} = {}\n'.format(n, m, round(float(n) - float(m), 2)))
        if novamente(x) == False:
            break
        
    if menu == 3:
        n = float(input('Digite o primeiro valor a ser multiplicado: '))
        m = float(input('Digite o segundo valor a ser multiplicado: '))
        print('O resultado de {} * {} = {}\n'.format(n, m, round(float(n) * float(m), 2)))
        if novamente(x) == False:
            break
        
    if menu == 4:
        n = float(input('Digite o dividendo: '))
        m = float(input('Digite o divisor: '))
        if m != 0:
            print('O resultado de {} / {} = {}\n'.format(n, m, round(float(n) / float(m), 2)))

        else:
            print('O divisor não pode ser nulo, tente novamente!')
        if novamente(x) == False:
            break

