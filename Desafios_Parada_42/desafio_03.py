# Faça um programa no qual o usuário precisa cadastrar as informações de dois produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total das compras.

codigo_prod1 = input('Digite o código do produto: ')
nome_prod1 = input('Informe o produto: ')
qtde_prod1 = int(input('Quantidade de produtos adquiridos: '))
preco_prod1 = float(input('Informe o preço do produto: R$'))

print(' ')

codigo_prod2 = input('Digite o código do produto: ')
nome_prod2 = input('Informe o produto: ')
qtde_prod2 = int(input('Quantidade de produtos adquiridos: '))
preco_prod2 = float(input('Informe o preço do produto: R$'))
print('')
total = (qtde_prod1 * preco_prod1) + (qtde_prod2 * preco_prod2)

print('='*15 + ' NOTA FISCAL ' + '='*15)
print(f'{codigo_prod1} -- {nome_prod1} -- {qtde_prod1} X R${preco_prod1}')
print(f'{codigo_prod2} -- {nome_prod2} -- {qtde_prod2} X R${preco_prod2}')
print(' ')
print(f'TOTAL DA COMPRA: R${total}')
print('='*43)
