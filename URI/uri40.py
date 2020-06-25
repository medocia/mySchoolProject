N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

avg = (float(N1)*2+float(N2)*3+float(N3)*4+float(N4))/10

if (avg >= 7):
	print("Media: %.1f" %avg)
	print("Aluno aprovado.")

elif (avg >= 5):
	print("Media: %.1f" %avg)
	print("Aluno em exame.")

	exam = input()
	exam = float(exam)

	avg2 = (avg+exam)/2

	if (avg2 >= 5):
		print("Nota do exame: %.1f" %exam)
		print("Aluno aprovado.")
		print("Media final: %.1f" %avg2)

	else:
		print("Nota do exame: %.1f" %exam)
		print("Aluno reprovado.")
		print("Media final: %.1f" %avg2)

else:
	print("Media: %.1f" %avg)
	print("Aluno reprovado.")



