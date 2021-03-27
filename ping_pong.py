import pygame

# Cores.
preto = 0, 0, 0
branco = 255, 255, 255
verde = 0, 255, 0

# Configurando a tela.
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
tela_retangulo = tela.get_rect()


class Raquete:
    def __int__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(verde)
        self.imagem_retangulo = self.imagem.get_rect()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


raquete = Raquete((10, 50))
fim = False

# Iniciando a tela.
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Condição de saida.
            fim = True
    tela.fill(preto)
    raquete.realiza()
    pygame.display.update()
