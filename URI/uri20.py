days = int(input())

years = int(days/365)
days -= years*365

months = int(days/30)
days -= months*30

print("%d ano(s)" %years)
print("%d mes(es)" %months)
print("%d dia(s)" %days)