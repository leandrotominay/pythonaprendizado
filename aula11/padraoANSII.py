from datetime import date

# ANSI - ESCAPE SEQUENCE \
# \033[(Estilo) (Cor do texto) e (Cor do fundo) m
# Estilos: 0 = None, 1 = Bold, 4 = Underline, 7 = Invert colors "negative"
# Cor do texto: 30 = branco, 31 = Vermelho, 32 = Verde, 33 = Amarelo, 34 = Azul, 35 = Roxo, 36 = Azul claro, 37 = Cinza
# Cor do fundo: 40 = branco, 41 = Vermelho, 42 = Verde, 43 = Amarelo, 44 = Azul, 45 = Roxo, 46 = Azul claro, 47 = Cinza
# \033[0;33;44m = Estilo nenhum, cor Amarela e fundo Azul
# \033[  m
# \033[  m

print("\033[0;33;44m Olá mundo!\033[m")
print("Sejam bem-vindos ao meu programa de estudos de \033[1;33;44mPython!\033[m")

data_atual = date.today()

data_em_texto = "\033[1;34;35m{}/{}/{}\033[m".format(data_atual.day, data_atual.month, data_atual.year)

print("A data de hoje é",data_em_texto)