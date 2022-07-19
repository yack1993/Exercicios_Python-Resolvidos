dias_alugados = int(input("Quantos dias alugados: "))
Km_rodados = float(input('Quantos KM rodados: '))

pago = (dias_alugados * 60) + (Km_rodados * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))