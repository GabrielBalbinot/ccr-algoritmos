n = int(input("Digite um número natural: "))

primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False

if primo:
    print("O número é primo")
else:
    print("O número não é primo")