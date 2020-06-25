N = int(input())

m = int(N/60)
N -= m*60
h = int(m/60)
m -= h*60

print(str(h)+":"+str(m)+":"+str(N))