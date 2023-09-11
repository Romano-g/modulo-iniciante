# numero = input('Digite um numero inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par = numero_int % 2 == 0
#     par_txt = 'ímpar'

#     if par:
#         par_txt = 'par'

#     print(f'O número {numero_int} é {par_txt}')

# else:
#     print('Não é um número inteiro')

# horas = input('Digite as horas: ')

# try:
#     horas_int = int(horas)

#     if horas_int <= 11:
#         print('Bom dia!')

#     elif horas_int >= 12 and horas_int <= 17:
#         print('Boa tarde!')

#     elif horas_int >= 18 and horas_int <= 23:
#         print('Boa noite!')

#     else:
#         print('Não conheço essa hora')

# except:
#     print('Não é uma hora inteira')

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