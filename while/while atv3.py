print('''
     Escolha qual operação matematica deseja
     
     [1] soma 
     [2] subtração
     [3] multiplicação
     [4] divisão
     
''')




persona = int(input(">>>  "))
if persona == 1:
    n1=int(input("escolha um numero: "))
    n2=int(input("escolha numero2: "))
    print(n1 + n2)

elif persona == 2:
    n1=int(input("escolha um numero: "))
    n2=int(input("escolha numero2: "))
    print(n1 - n2)

elif persona == 3:
    n1=int(input("escolha um numero: "))
    n2=int(input("escolha numero2: "))
    print(n1 * n2)

elif persona == 4:
    n1=int(input("escolha um numero: "))
    n2=int(input("escolha numero2: "))
    print(n1 / n2)