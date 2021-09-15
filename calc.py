import math as m

print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
print('5 - Potenciação\n6 - Raiz quadrada\n7 - Raiz Cúbica\n8 - Logaritmo')
print('9 - Equação de 2º Grau\n0 - Sair\n')
menu = int(input("Digite a operação desejada: "))
print('')

#Função para realizar novamente o uso da calculadora#
def novamente():
    r = str(input('Gostaria de continuar?[s/n] '))
    if r in 'nN':
        print('Obrigado por confiar nos meus cálculos, volte logo!')
        return False
    if r in 'sS':
        return True
    else:
        print('Informe uma opção válida')
        return novamente()

#Equação do 2º grau
def equacao():
    a_dig = float(input('Digite o valor de a: '))
    b_dig = float(input('Digite o valor de b: '))
    c_dig = float(input('Digite o valor de c: '))
    print_raiz(a_dig, b_dig, c_dig)
    
def delta(a,b,c):
    return b ** 2 - 4 * a * c

def print_raiz(a,b,c):
    d = delta(a,b,c)
    if d == 0:
        raiz1 = (-b)/(2*a)
    else:
        if d < 0:
            print('Esta equação não possuí raizes reais')
        else:
            raiz1 = (-b - m.sqrt(d)) / (2 * a)
            raiz2 = (-b + m.sqrt(d)) / (2 * a)
            print('\nA primeira raiz é', raiz1)
            print('A segunda raiz é', raiz2)
if menu == 0:
    print('Tudo bem, estarei te aguardando!')

while menu != 0:
    if menu not in range(0,10):
        print('Eiiiii! Essa opção não existe, tente novamente!\n')
        menu = int(input('Digite a operação desejada: '))
    #soma        
    if menu == 1:
        n = float(input('Digite o primeiro valor a ser somado: '))
        m = float(input('Digite o segundo valor a ser somado: '))
        print('O resultado de {} + {} = {}\n'.format(n, m, round(float(n) + float(m), 2)))
        
    #subtração
    if menu == 2:
        n = float(input('Digite o primeiro valor a ser subtraído: '))
        m = float(input('Digite o segundo valor a ser subtraído: '))
        print('O resultado de {} - {} = {}\n'.format(n, m, round(float(n) - float(m), 2)))
 
    #multiplicação    
    if menu == 3:
        n = float(input('Digite o primeiro valor a ser multiplicado: '))
        m = float(input('Digite o segundo valor a ser multiplicado: '))
        print('O resultado de {} * {} = {}\n'.format(n, m, round(float(n) * float(m), 2)))
 
    #divisão    
    if menu == 4:
        n = float(input('Digite o dividendo: '))
        m = float(input('Digite o divisor: '))
        if m != 0:
            print('O resultado de {} / {} = {}\n'.format(n, m, round(float(n) / float(m), 2)))
        #regra para o divisor diferente de 0
        else:
            print('O divisor não pode ser nulo, tente novamente!')

    #potenciação    
    if menu == 5:
        n = float(input('Digite o valor da base: '))
        m = float(input('Digite o valor do expoente: '))
        print('O resultado de {}^{} = {}\n'.format(n, m, round(float(n) ** float(m), 2)))

    #raiz quadrada
    if menu == 6:
        n = float(input('Digite o valor do radicando: '))
        print('A raiz quadrada de {} é = {}\n'.format(n, float(m.sqrt(n))))

    #raiz cúbica
    if menu == 7:
        n = float(input('Digite o valor do radicando: '))
        print('A raiz cúbica de {} é = {}\n'.format(n, float(n) ** (1/3)))
    
    #logaritmo
    if menu == 8:
        n = float(input('Digite o valor do logaritmando: '))
        base = float(input('Digite o valor da base: '))
        print('O resultado do logaritmo de {} na base {} = {}\n'.format(n, base, (m.log(n)/m.log(base))))
    
    #equação de 2º grau
    if menu == 9:
        equacao()

    if novamente() == False:
        break
