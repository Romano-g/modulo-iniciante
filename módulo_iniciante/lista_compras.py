import os

lista = []

while True:
    pergunta = input(f'Selecione uma opção\n[i]nserir, [a]pagar, [l]istar ou [s]air: ')

    if pergunta == 'i':
        os.system('cls')
        item = input('Qual valor quer adicionar? ')
        lista.append(item)
        os.system('cls')

    elif pergunta == 'a':
        try:
            os.system('cls')
            apagar = input('Qual item quer apagar? ')
            apagar = int(apagar)
            del lista[apagar]
            os.system('cls')

        except:
            os.system('cls')
            print('Esse índice não existe.')

    elif pergunta == 'l':
        for indice, nome in enumerate(lista):
            print(indice, nome)

        if lista == []: # ou if len(lista) == 0
            os.system('cls')
            print('Não há o que exibir.')

    else:
        os.system('cls')
        print('Você saiu da lista de compras.')
        break