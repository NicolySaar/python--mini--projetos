algo = input("Digite algo: ")

print('O tipo primitivo desse valor é ',type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('Está em maiúsculo? ', algo.isupper())
print('Está em minúsculo? ', algo.islower())
print('Está capitalizada? ', algo.istitle())