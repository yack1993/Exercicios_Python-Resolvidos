n1 = float(input("Digite a 1ª nota do aluno: "))
n2 = float(input("Digite a 2ª nota do aluno: "))

media = (n1 + n2) / 2
#:1f um digito depois da virgula
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, media))
