def gerar_mapa_base():

    mapa = []
    mapa_altura = 100   
    mapa_largura = 75

    for _ in range(mapa_altura):
        linha = []
        for _ in range(mapa_largura):
            linha.append("#")
        mapa.append(linha)
    return mapa

class Sala:

    def __init__(self, y, x, largura, altura):
        self.y = y
        self.x = x
        self.largura = largura
        self.altura = altura

def esculpir_sala_no_mapa(mapa, sala):
    for y in range(sala.y, sala.y + sala.altura):
        for x in range(sala.x, sala.x + sala.largura):
            mapa[y][x] = "."
    
    return mapa

mapa_base = gerar_mapa_base()
minha_sala = Sala(x=5, y=5, largura=20, altura=10)

esculpir_sala_no_mapa(mapa_base, minha_sala)

print("\n--- Mapa da Masmorra ---")
for linha in mapa_base:
    print("".join(linha))