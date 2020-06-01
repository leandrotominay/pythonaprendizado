# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato brasileiro de futebol. Depois mostre
# 1. Apenas os 5 primeiros colocados.
# 2. Os últimos 4 colocados da tabela.
# 3. Uma lista com os times em ordem alfabética
# 4. Em que posição na tabela está o time da Chapecoense

times = 'Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza EC','Goiás','Bahia','Vasco da Gama','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí'

print("Os primeiros colocados da tabela do Brasileirão são: ")
for cont in range(0, 5):
    print(f'{cont + 1} - {times[cont]} ')

print("Os últimos 4 colocados da tabela são: ")
for cont in range(19, 15, -1):
    print(f'{cont + 1} - {times[cont]} ')
sorteados = sorted(times)

print("A lista dos times em ordem alfabética:")
for cont in range(0,20):
    print(f'{sorteados[cont]}')

print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição")

