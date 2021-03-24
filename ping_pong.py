import pygame

# Cores.
preto = 0, 0, 0
branco = 255, 255, 255

# Configurando a tela.
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)

fim = False

# Iniciando a tela.
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Condição de saida.
            fim = True
    tela.fill(preto)
    pygame.display.update()
