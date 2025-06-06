# fontes da letra
print('')
print('\033[0m(editar)\033[m') # nenhuma fonte
print('\033[1m(editar)\033[m') # negrito
print('\033[4m(editar)\033[m') # sublinhado
print('\033[7m(editar)\033[m') # reverso
print('')

# cor do text 
print('\033[30m(editar)\033[m') # cinza
print('\033[31m(editar)\033[m') # vermelho
print('\033[32m(editar)\033[m') # verde
print('\033[33m(editar)\033[m') # amarelo
print('\033[34m(editar)\033[m') # azul
print('\033[35m(editar)\033[m') # roxo
print('\033[36m(editar)\033[m') # ciano
print('\033[37m(editar)\033[m') # cinza claro
print('')

# cor do fundo
print('\033[40m(editar)\033[m') # preto
print('\033[41m(editar)\033[m') # vermelho
print('\033[42m(editar)\033[m') # verde
print('\033[43m(editar)\033[m') # amarelo
print('\033[44m(editar)\033[m') # azul
print('\033[45m(editar)\033[m') # roxo
print('\033[46m(editar)\033[m') # ciano
print('\033[47m(editar)\033[m') # cinza claro


# estilo personalizado
print('\033[31;40m(editar)\033[m') # fundo preto texto vermelho
def texto(t):
    return '\033[31;40m{}\033[m'.format(t)



print('\033[0m(padrão)\033[m') # voltar ao padrão
def padrao(t):
    return '\033[0m{}\033[m'.format(t)



print(texto('eu quero gozar'))
