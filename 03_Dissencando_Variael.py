a = input("Digite algo: ")
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabenúmerico",  a.isalnum())
print("Esta em maiúscula? ", a.isupper())
print("Está em minúscula? ", a.islower())
print("Está capitalizada? ", a.istitle())