A, B, C = input().split(" ")
D, E, F = input().split(" ")

code1, unit1, value1 = A, B, C
code2, unit2, value2 = D, E, F

total = (int(unit1)*float(value1))+(int(unit2)*float(value2))
print("VALOR A PAGAR: R$ %.02f" %total)