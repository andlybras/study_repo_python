import random

MAPA_LARGURA = 100
MAPA_ALTURA = 100

def gerar_mapa_base():
    mapa = []

    for _ in range(MAPA_ALTURA):
        linha = []
        for _ in range(MAPA_LARGURA):
            linha.append("#")
        mapa.append(linha)
    return mapa

class Sala:

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

def gerar_sala_aleatoria():
    sala_largura = random.randint(5, 25)
    sala_altura = random.randint(5, 25)

    sala_x = random.randint(1, MAPA_LARGURA - sala_largura - 1)
    sala_y = random.randint(1, MAPA_ALTURA - sala_altura - 1)

    return Sala(sala_x, sala_y, sala_largura, sala_altura)

def esculpir_sala_no_mapa(mapa, sala):
    for y in range(sala.y, sala.y + sala.altura):
        for x in range(sala.x, sala.x + sala.largura):
            mapa[y][x] = "."
    return mapa

mapa_base = gerar_mapa_base()
sala_aleatoria = gerar_sala_aleatoria()
esculpir_sala_no_mapa(mapa_base, sala_aleatoria)

print("\n--- Mapa da Masmorra ---")
for linha in mapa_base:
    print("".join(linha))