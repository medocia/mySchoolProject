money = float(input())

money = int(money*100)

banknotes = [100,50,20,10,5,2]
coins = [1,0.5,0.25,0.10,0.05,0.01]

resBanknotes = []
resCoins = []

for banknote in banknotes:
	number = money//(banknote*100)
	money -= (number*(banknote*100))
	resBanknotes.append(number)

for coin in coins:
	number = money//(coin*100)
	money -= (number*(coin*100))
	resCoins.append(number)

print("NOTAS:")

for i in range(len(banknotes)):
	print("%i nota(s) de R$ %.2f" %(resBanknotes[i], banknotes[i]))

print("MOEDAS:")

for i in range(len(coins)):
	print("%i moeda(s) de R$ %.2f" %(resCoins[i], coins[i]))



