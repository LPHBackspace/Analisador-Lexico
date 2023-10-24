# Array Lexemas
lexemas = []
palavra_atual = ''

# abrir codigo
with open('program.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        for letra in linha:
            if letra in 'abcdefghijklmnopqrstuvwxyz':
                palavra_atual += letra
            else:
                if palavra_atual == '':
                     lexemas.append(letra)
                else:
                    lexemas.append(palavra_atual)
                    palavra_atual = ''
                    if letra != '':
                        lexemas.append(letra)

i = len(lexemas) - 1
while i >= 0:
    if lexemas[i] == '' or lexemas[i] == ' ':
        del lexemas[i]
    i -= 1


print(lexemas)