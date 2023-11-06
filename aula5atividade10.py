maior = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break

    if num > maior:
        maior = num
print("\nO maior valor é", maior)