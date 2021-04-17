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
tempo = pygame.time.Clock()
pygame.display.set_caption('Pong')


class Raquete:
    def __int__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(verde)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15
        self.imagem_retangulo[0] = 0

    def mover(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

    def atualizar(self, tecla):
        if tecla[pygame.K_UP]:
            self.move(0, -1)

        if tecla[pygame.K_DOWN]:
            self.move(0, 1)
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


class Bola:
    def __int__(self, tamanho):
        self.altura, self.largura = tamanho
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(vermelho)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 10
        self.flag = False
        self.set_bola()

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -.5 and num < 0.5:
                continue
            else:
                return num

    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.imagem_retangulo.x = tela_retangulo.centerx
        self.imagem_retangulo.y = tela_retangulo.centery
        self.velo = [x, y]
        self.pos = list(tela_retangulo.center)

    def colide_parede(self):
        if self.imagem_retangulo.y < 0 or self.imagem_retangulo.y > tela_retangulo.bottom - self.altura:
            self.velo[1] *= -1
            self.flag = False
        if self.imagem_retangulo.x < 0 or self.imagem_retangulo.x > tela_retangulo.right - self.largura:
            self.velo[0] *= -1
            if self.imagem_retangulo.x < 0 and self.flag == False:
                placar.pontos -= 1
                print('Bateu na parede!')
                self.flag = True

    def colide_raquete(self, raquete_rect):
        if self.imagem_retangulo.colliderect(raquete_rect):
            self.velo[0] *= -1
            self.velocidade += 1
            placar.pontos += 1
            print('Boa!')

    def move(self):
        self.pos[0] += self.velo[0] * self.velocidade
        self.pos[1] += self.velo[1] * self.velocidade
        self.imagem_retangulo.center = self.pos

    def atualizar(self, raquete_rect):
        self.colide_parede()
        self.colide_raquete(raquete_rect)
        self.move()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)


class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 10

    def contagem(self):
        self.text = self.fonte.render('pontos = ' + str(self.pontos), 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = tela.get_width() / 2
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))


raquete = Raquete((10, 50))
bola = Bola((15, 15))
placar = Placar()

# Iniciando a tela.
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Condição de saida.
            fim = True
    tecla = pygame.key.get_pressed()
    tela.fill(preto)
    raquete.realiza()
    bola.realiza()
    raquete.atualizar(tecla)
    bola.atualizar(raquete.imagem_retangulo)
    tempo.tick(30)
    placar.contagem()
    pygame.display.update()
