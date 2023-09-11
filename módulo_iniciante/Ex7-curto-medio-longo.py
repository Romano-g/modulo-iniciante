nome = input('Digite seu nome: ')
curto = len(nome) <= 4
normal = len(nome) >= 5 and len(nome) <= 6
grande = len(nome) > 6

try:
    if curto:
        print('Seu nome é curto')
    elif normal:
        print('Seu nome é normal')
    elif grande:
        print('Seu nome é muito grande')

except:
    ...
