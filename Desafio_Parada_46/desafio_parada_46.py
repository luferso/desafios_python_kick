def a_vista(valor):
        total = valor - (valor *0.15)
        print(f'Você teve um desconto de 15% e o valor a ser pago é de R${total:.2f}')

def parcelado(valor):
        entrada = int(input('Você gostaria de dar um valor de entrada?\n 1- Sim \n 2- Não \n Escolha uma opção: '))
        if entrada == 1:
            valor_entrada = int(input('Qual o valor que gostaria de pagar como entrada?\n R$ '))
            valor = valor - valor_entrada
        parcelas = int(input('Em quantas parcelas gostaria de dividir o pagamento?\n '))
        if 0 < parcelas <= 10:
            total = valor / parcelas
            print(f'O valor de R${valor} será dividido sem juros em {parcelas} parcelas de R${total:.2f} cada.')
        elif parcelas > 10:
            total = ((valor*1.10) / parcelas)
            print(f'O valor de R${valor} será dividido com juros de 10% em {parcelas} parcelas de R${total:.2f} cada.')
        else:
            print('Quantidade de parcelas inválido. Programa encerrado')

def pagamento():
    valor = float(input('Qual o valor a ser pago?\nR$ '))
    opcao_pagamento = int(input('Qual a forma de pagamento? \n 1 - À vista \n 2 - Parcelado \n Escolha uma opção: '))
    if opcao_pagamento == 1:
        a_vista(valor) 
    else:
        parcelado(valor)
 
def main():
    pagamento()

main()