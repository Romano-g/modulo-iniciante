while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+/-/*//): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = False

    if numeros_validos is None:
        print('Um dos números é invalido.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)

    sair = input('Quer sair? [s] ou [n]: ').lower().startswith('s')
    
    if sair is True:
        break