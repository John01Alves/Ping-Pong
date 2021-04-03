import pygame

# Cores.
preto = 0, 0, 0
branco = 255, 255, 255
verde = 0, 255, 0

fim = False

# Configurando a tela.
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
tela_retangulo = tela.get_rect()


class Raquete:
    def __int__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(verde)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15
        self.imagem_retangulo[0] = 20

    def mover(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

    def atualizar(self, tecla):
        if tecla[pygame.K_UP]:
            self.mover(0, -1)

        if tecla[pygame.K_DOWN]:
            self.mover(0, 1)
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

raquete = Raquete((10, 50))

# Iniciando a tela.
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Condição de saida.
            fim = True
    tecla = pygame.key.get_pressed()
    tela.fill(preto)
    raquete.realiza()
    raquete.atualizar(tecla)
    pygame.display.update()
