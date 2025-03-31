numsitivo = float(input("digite um numero positivo: "))
while numsitivo >= 0:
    print("seu numero é positivo")
    break
while numsitivo < 0:
    print("tente novamente, mas agr com um numero positivo")
    numsitivo = float(input("digite novamente: "))
    if numsitivo >= 0:
        print("seu numero é postivo")