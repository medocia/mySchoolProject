n = int(input())

banknotes = [100, 50, 20, 10, 5]

print("Pecahan uang Kakek Brian : ")

for banknote in banknotes:
  qt_cedulas = int((n/1000)/banknote)
  n -= qt_cedulas * banknote
  print("%d Lembar Uang %drb" %(qt_cedulas, banknote))