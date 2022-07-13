produto = float(input('Informe o preço deste produto: '))

novo_preco = produto - ((produto * 5) / 100)

print('O produto custava R${}, na promoção de 5% var custar {:.2f}!'.format(produto, novo_preco))