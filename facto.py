str_n = input('Veuillez saisir un nombre : ')
n = int(str_n)
factorial = 1
for i in range(2, n+1):
    print(i)
    factorial = factorial * i
print(n,'! =', factorial)
