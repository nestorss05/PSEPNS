num = int(input("Inserta un numero para factorial: "))
sol = int(num)
for contador in range(num-1, 0, -1):
    sol = sol * contador
print(sol)