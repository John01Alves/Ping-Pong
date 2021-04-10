import pygame
import random

# Cores.
preto = 0, 0, 0
branco = 255, 255, 255
verde = 0, 255, 0
vermelho = 255, 0, 0

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


class Bola:
    def __int__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(vermelho)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 1
        self.set_bola()

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -0.5 and num < 0.5:
                continue
            else:
                return num

    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.imagem_retangulo.x = tela_retangulo.centerx
        self.imagem_retangulo.y = tela_retangulo.centery
        self.velo = [x, y]

    def mover(self):
        self.imagem_retangulo[0] += self.velo[0] * self.velocidade
        self.imagem_retangulo[1] += self.velo[1] * self.velocidade

    def atualizar(self):
        self.move()
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

raquete = Raquete((10, 50))
bola = Bola((15, 15))

# Iniciando a tela.
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Condição de saida.
            fim = True
    tecla = pygame.key.get_pressed()
    tela.fill(preto)
    raquete.realiza()
    raquete.atualizar(tecla)
    bola.realiza()
    bola.atualizar()
    pygame.display.update()
