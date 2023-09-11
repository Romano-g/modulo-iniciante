frase = 'Lorem ipsum nisl litora convallis tempor ipsum dapibus cras praesent purus, egestas dictum sollicitudin senectus dictumst faucibus ornare commodo. iaculis taciti egestas imperdiet varius morbi sem torquent cubilia, senectus tincidunt morbi augue etiam eros nulla, vulputate donec ac lacinia enim imperdiet malesuada. felis class orci scelerisque sed adipiscing torquent curae sollicitudin commodo, iaculis quisque sollicitudin viverra sodales dictumst habitasse diam netus ut, dictumst ante eros pulvinar litora purus lorem nec. mauris per enim curabitur sollicitudin facilisis metus gravida, sapien sem dapibus maecenas pulvinar quam, leo lorem sem felis arcu tortor. \
	Morbi consequat sollicitudin ad adipiscing vehicula senectus ut donec pretium odio, aenean per platea enim pharetra semper sagittis felis. orci auctor purus senectus erat risus condimentum enim justo vitae duis aliquet, primis erat fermentum non neque tincidunt ultrices a urna taciti, sem metus nisi eros aliquam donec imperdiet cubilia posuere diam. cras enim cursus accumsan gravida ligula volutpat, nibh ornare aliquam dui est, consectetur quis quisque pharetra ac. eleifend molestie curae condimentum purus proin imperdiet rhoncus sagittis, velit dui ultrices nibh orci cras aliquam eros, nisl euismod ac tempor faucibus justo litora. \
	Potenti semper class proin mi egestas augue, eu sapien arcu dapibus at enim, hac eu odio lectus molestie. '

# i = 0
apareceu_mais = 0
letra_apareceu_mais = ''

# while i < len(frase):
    # letra_atual = frase[i]
for letra in frase:

    if letra == ' ':
        # i += 1
        continue

    vezes = frase.count(letra) 

    if apareceu_mais < vezes:
        apareceu_mais = vezes
        letra_apareceu_mais = letra

    # i += 1

print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais}, que apareceu {apareceu_mais}x.')