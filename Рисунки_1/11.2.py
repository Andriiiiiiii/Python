import pygame

pygame.init()

FPS = 30
sx = 1000
sy = 700
screen = pygame.display.set_mode((sx, sy))

b = (200, 200, 200)
gray = (224, 255, 255)
fish = (140, 170, 170)
black = (20, 20, 20)
blue = (0, 0, 255)
red = (255, 50, 50)
snow = (249, 249, 249)
back = (230, 230, 230)
col1 = (140, 120, 110)
col2 = (110, 90, 80)
col3 = (220, 210, 210)


pygame.draw.rect(screen, back, (0, 0, sx, sy / 2.5))
pygame.draw.rect(screen, snow, (0, sy / 2.5, sx, sy))

def human(x, y, scale, orientation):
    s1 = pygame.Surface((sx, sy), pygame.SRCALPHA)

    pygame.draw.ellipse(s1, col1, (100, 100, 80, 50))
    pygame.draw.ellipse(s1, col1, (90, 140, 100, 180))
    pygame.draw.rect(s1, snow, (90, 235, 100, 100))
    pygame.draw.ellipse(s1, col1, (150, 220, 25, 40))
    pygame.draw.ellipse(s1, col1, (110, 220, 25, 40))
    pygame.draw.ellipse(s1, col1, (95, 250, 35, 10))
    pygame.draw.ellipse(s1, col1, (155, 250, 35, 10))
    pygame.draw.rect(s1, col2, (90, 230, 100, 10))
    pygame.draw.rect(s1, col2, (130, 150, 20, 80))
    pygame.draw.ellipse(s1, col1, (70, 170, 40, 20))
    pygame.draw.aaline(s1, black, (75, 120), (80, 250), 2)
    pygame.draw.ellipse(s1, col3, (115, 110, 50, 30))
    pygame.draw.line(s1, black, (126, 116), (132, 120), 2)
    pygame.draw.line(s1, black, (143, 121), (150, 116), 2)
    pygame.draw.lines(s1, black, 3, (
        (130, 133), (138, 131), (145, 135)), 2)

    s3 = pygame.Surface((80, 40))
    pygame.Surface.set_colorkey(s3,(0, 0, 0))
    pygame.draw.ellipse(s3, col1, (0, 0, 40, 20))
    s3 = pygame.transform.rotate(s3, -30)
    s1.blit(s3, (155, 164))

    s2 = pygame.Surface((sx, sy))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    s2.set_alpha(100)
    pygame.draw.ellipse(s2, col1, (90, 90, 100, 70))
    s1.blit(s2, (0, 0))

    if not orientation:
        s1 = pygame.transform.flip(s1, True, False)
    if scale < 1:
        s1 = pygame.transform.smoothscale(s1, (round(sx * scale), round(sy * scale)))
    if scale > 1:
        s1 = pygame.transform.scale(s1, (round(sx * scale), round(sy * scale)))
    screen.blit(s1, (x-100, y-100))


def bear(x, y, scale, orientation):
    s1 = pygame.Surface((200, 200), pygame.SRCALPHA)

    pygame.draw.ellipse(s1, b, (50, 50, 80, 30))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, b, (0, 0, 70, 15))
    s2 = pygame.transform.rotate(s2, 30)
    s1.blit(s2, (110, 33))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, b, (0, 0, 50, 15))
    s2 = pygame.transform.rotate(s2, -70)
    s1.blit(s2, (100, 50))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, b, (0, 0, 50, 15))
    s2 = pygame.transform.rotate(s2, -80)
    s1.blit(s2, (87, 53))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, b, (0, 0, 50, 14))
    s2 = pygame.transform.rotate(s2, -110)
    s1.blit(s2, (45, 50))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, b, (0, 0, 50, 14))
    s2 = pygame.transform.rotate(s2, -120)
    s1.blit(s2, (21, 47))

    s2 = pygame.Surface((70, 20))
    pygame.Surface.set_colorkey(s2,(0, 0, 0))
    pygame.draw.ellipse(s2, fish, (0, 0, 35, 15))
    pygame.draw.polygon(s2, fish, [[33, 8], [43, 15], [43, 0]])
    pygame.draw.circle(s2, blue, (6, 8), 3)
    pygame.draw.polygon(s2, red, [[12, 13], [20, 13], [16, 18]])
    s2 = pygame.transform.rotate(s2, -20)
    s1.blit(s2, (21, 47))

    pygame.draw.ellipse(s1, b, (35, 30, 40, 30))
    pygame.draw.polygon(s1, b, ((40, 35), (50, 31), (45, 20)))
    pygame.draw.polygon(s1, b, ((55, 35), (65, 31), (60, 20)))
    pygame.draw.circle(s1, snow, (45, 44), 4)
    pygame.draw.circle(s1, snow, (58, 44), 4)
    pygame.draw.circle(s1, black, (47, 44), 1)
    pygame.draw.circle(s1, black, (60, 44), 1)
    pygame.draw.circle(s1, black, (50, 50), 1)
    pygame.draw.polygon(s1, snow, ((52, 59), (48, 58), (49, 62)))
    pygame.draw.polygon(s1, snow, ((45, 55), (41, 54), (43, 59)))

    if not orientation:
        s1 = pygame.transform.flip(s1, True, False)
    if scale < 1:
        s1 = pygame.transform.smoothscale(s1, (round(200 * scale), round(200 * scale)))
    if scale > 1:
        s1 = pygame.transform.scale(s1, (round(200 * scale), round(200 * scale)))
    screen.blit(s1, (x - 50, y - 50))


def home(x, y, scale, orientation):
    s1 = pygame.Surface((sx, sy))
    pygame.Surface.set_colorkey(s1,(0, 0, 0))

    pygame.draw.circle(s1, gray, (125, 350), 100, 0, 1, 1, 0, 0)
    pygame.draw.circle(s1, black, (125, 350), 100, 3, 1, 1, 0, 0)

    pygame.draw.line(s1, black, (70, 270), (180, 270))
    pygame.draw.line(s1, black, (40, 300), (210, 300))
    pygame.draw.line(s1, black, (30, 330), (220, 330))
    pygame.draw.line(s1, black, (20, 350), (230, 350))
    pygame.draw.line(s1, black, (125, 250), (125, 270))
    pygame.draw.line(s1, black, (90, 270), (90, 300))
    pygame.draw.line(s1, black, (160, 270), (160, 300))
    pygame.draw.line(s1, black, (125, 300), (125, 330))
    pygame.draw.line(s1, black, (195, 300), (195, 330))
    pygame.draw.line(s1, black, (55, 300), (55, 330))
    pygame.draw.line(s1, black, (90, 330), (90, 350))
    pygame.draw.line(s1, black, (160, 330), (160, 350))

    if not orientation:
        s1 = pygame.transform.flip(s1, True, False)
    if scale < 1:
        s1 = pygame.transform.smoothscale(s1, (round(sx * scale), round(sy * scale)))
    if scale > 1:
        s1 = pygame.transform.scale(s1, (round(sx * scale), round(sy * scale)))

    screen.blit(s1, (x - 125, y - 350))


home(200, 450, 0.6, True)
home(125, 450, 0.8, True)
home(400, 370, 1, True)

human(400, 390, 0.6, True)
human(350, 480, 0.7, True)
human(150, 400, 1, False)
human(400, 390, 0.3, False)


bear(90, 410, 1, False)
bear(50, 500, 0.7, True)
bear(140, 500, 1.1, False)
bear(500, 500, 0.8, False)
bear(650, 450, 0.5, False)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("[", event.pos[0], ",", event.pos[1], "],")

pygame.quit()
