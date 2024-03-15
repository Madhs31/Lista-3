#População A - 80000 habitantes - taxa de crescimento 3% - ou seja, 2400 pessoas a cada ano
#Pupolação B - 200000 - taxa de crescimento de 1.5% - ou seja, 3 mil a cada ano
# programa que calcule a quantidade de anos necessários para alcançar o b ou ficar igual
A=80000
B=200000
anos=0
while (A <= B):
	A=A+(A*0.03)
	B=B+(B*0.015)
	anos=anos+1
print(anos)	