banknotes = [100,50,20,10,5,2]
coins = [1,0.5,0.25,0.10,0.05,0.01]
money = float(input())

for banknote in banknotes:
	number = int(money/banknote)
	money -= number*banknote

print("NOTAS:")
print("%d nota(s) de R$ %.2f" %(number, banknote))

for coin in coins:
	number = int(money/coin)
	money -= number*banknote

print("MOEDAS:")
print("%d moeda(s) de R$ %.2f" %(number, coin))

