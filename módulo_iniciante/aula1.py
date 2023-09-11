"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input ('Digite um número inteiro: ')
# numero_int = int(numero)

# par = numero_int % 2 == 0
# impar = numero_int % 2  != 0


# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_txt = 'ímpar'

#     if par_impar:
#         par_impar_txt = 'par'

#     print(f'O número {numero_int} é {par_impar_txt}')

# else:
#     print('Não é um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Digite o horário: ')
# horario_int = int(horario)
# BOM_DIA = horario_int <= 11
# BOA_TARDE = horario_int >= 12 and horario_int <= 17
# BOA_NOITE = horario_int >= 18 and horario_int <= 24

# if BOM_DIA:
#     print('Bom dia!')

# if BOA_TARDE:
#     print('Boa tarde!')

# if BOA_NOITE:
#     print('Boa noite!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu nome: ')
# curto = len(nome) <= 4
# normal = len(nome) >= 5 and len(nome) <= 6
# grande = len(nome) > 6

# if curto:
#     print('Seu nome é curto')
# if normal:
#     print('Seu nome é normal')
# if grande:
#     print('Seu nome é muito grande')