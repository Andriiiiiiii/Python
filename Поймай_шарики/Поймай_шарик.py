import pygame
from random import randint



pygame.display.set_caption("Поймай шарики")

class rectballs:

    
    def __init__(self, typ, time):
        self.typ = typ  # тип объекта
        self.time = time  # время
        self.color = COLORS[0] # цвет
        self.x = 0  # абсцисса
        self.y = 0  # ордината
        self.r = 0  # радиус объекта
        self.v_x = 0  # скорость по оси абсцисс
        self.v_y = 0  # скорость по оси ординат
        self.g_y = 0  # ускорение по оси ординат
        

    def move(self):
        '''
        Рассчитывает перемещение фигуры, заменяет пойманные на новые
        по истечении времени жизни фигуры. Отрисовывает все существующие фигуры
        '''
        self.move_count()  # Расчет новых параметров объекта
        self.draw()  # Отрисовка объекта


    def move_count(self):
        '''
        Отвечает за расчет новых параметров движения объекта, в том числе
        создание новых объектов по истечении времени жизини T_life
        '''
        if (self.time >= T_life) and (self.r == 0):  # cоздание нового объекта по истечению времени жизни старого, если его поймали
            self.new()
        else:
            self.x += self.v_x
            self.y += self.v_y
            self.v_y += self.g_y
            self.time += 1
            
            # отражение от стенок
            if (self.x+self.r) >= WIDTH:
                self.v_x *= -1
            if (self.x-self.r) <= 0:
                self.v_x *= -1
            if (self.y+self.r) >= HEIGHT:
                self.v_y *= -1
            if (self.y-self.r) <= 0:
                self.v_y *= -1


    def new(self):
        '''
        "Создает" (то есть сохраняет информацию) новый объект произвольного размера в случайном месте
        '''
        
        self.time = 0
        self.color = COLORS[randint(1, 6)]
        self.x = randint(0.1 * WIDTH, 0.9 * WIDTH)
        self.y = randint(0.1 * HEIGHT, 0.9 * HEIGHT)
        
        if self.typ == 0: #Для шара
            self.r = randint(0.02 * min(SIZE), 0.05 * min(SIZE))
            self.v_x = WIDTH / randint(4, 10) / FPS
            self.v_y = 0
            self.g_y = 0.7
            
        else: #Для квадрата
            self.r = randint(0.05 * min(SIZE), 0.1 * min(SIZE)) #Полусторона
            self.v_x = WIDTH / randint(2, 7) / FPS
            self.v_y = HEIGHT / randint(1, 4) / FPS
            self.g_y = 0

    def draw(self):   
        '''
        Рисует объект
        '''
        
        if self.typ == 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        else:
            pygame.draw.rect(screen, self.color, (self.x - self.r, self.y - self.r,
                                                  2*self.r, 2*self.r))
            

    def check(self, pos_mouse, button):
        '''
        Проверяет, попали ли кликом в один из объектов
        :param pos_mouse: кортеж из двух координат положения мыши
        :param button: номер кнопки мыши
        '''
        points = 0
        if (self.typ == 0)  and (((pos_mouse[0] - self.x)**2 + (pos_mouse[1] - self.y)**2) < self.r**2):
            self.r = 0 #Радиус шара нулевой
            points += 2
            
        if (self.typ == 1)  and (abs(pos_mouse[0] - self.x) < self.r) and (abs(pos_mouse[1] - self.y) < self.r):
            self.r = 0 #Полусторона квадрата нулевая
            points += 1
        
        return points

    
def const_colors():
    '''
    Задаем основные цвета, используемые в программе.
    Функция возвращает список из 7 цветов:
    черный, красный, синий, желтый, зеленый, маджента, цвет морской волны
    '''
    
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    colors = [black, red, blue, yellow, green, magenta, cyan]
    return colors

def screen_update():
    '''
    Рассчитывает перемещения объектов, заменяет пойманные на новые
    по истечении времени жизни объекта.
    Отрисовывает новое изображение на экране
    '''
    
    screen.fill(COLORS[0])  # Экран в черный
    for i in range(NUM_BALLS + NUM_RECTS):
        figures[i].move()  # Расчет новых параметров объекта и его отрисовка
    pygame.display.update()
    
def button_down(pos_mouse, button):
    '''
    Обрабатывает нажатие кнопки мыши
    :param pos_mouse: кортеж из двух координат положения мыши
    :param button: номер кнопки мыши
    Возвращает количество набранных баллов
    '''
    points = 0   
    for i in range(NUM_BALLS + NUM_RECTS):
            points += figures[i].check(button, pos_mouse)
    return points


def end(score):
    fin_score = 1000 - (int(score)*7)
    print("Смерть. Вы досчитали до:", fin_score)
    with open('Rating.txt', 'a') as file:
        file.write(str(fin_score) + ' ' + NAME + '\n')

NAME = input("Введи своё имя:  ")
print(NAME + ", ты попал на пытки к Гулю.")
print("Что бы ты не потерял сознание, отнимай от 1000 - 7, затем от 993 - 7 и т. д.")
print("Если ты досчитаешь до 0, то Гуль тебя отпустит")

T_life = 2
T = 10
NUM_BALLS = 7  # наибольшее число шаров, одновременно присутствующих на экране
NUM_RECTS = 9  # наибольшее число квадратов, одновременно присутствующих на экране

FPS = 30
SIZE = WIDTH, HEIGHT = 800, 600  # размер окна
screen = pygame.display.set_mode(SIZE)
T_life *= FPS  # перерасчет времени жизни в количество проходов цикла
COLORS = const_colors()
TIME = 0
score = 0  # счет
figures = []  # кортеж объектов класса rectballs
pygame.init()
pygame.mixer.music.load("fon.mp3")
pygame.mixer.music.play(-1)


for i in range(NUM_BALLS):
    figures.append(rectballs(0, T_life * (i+1) / NUM_BALLS))
for i in range(NUM_RECTS):
    figures.append(rectballs(1, T_life * (i+1) / NUM_RECTS))

    
pygame.init()
clock = pygame.time.Clock()
finished = False
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            delt = button_down(event.button, event.pos)
            score += delt

    screen_update() #Прорисовка сдвинутых объектов
    p1 = 1000 - 7*score
    TIME += 1
    if TIME % FPS == 0:
        print(p1)
    if TIME >= T*FPS + score*FPS/4:
        end(score)
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play(-1)
        finished = True
    if p1 <= 0:
        print(NAME + ", молодец! Ты выжил.")
        with open('Rating.txt', 'a') as file:
            file.write(str(fin_score) + ' ' + NAME + '\n')
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play(-1)
        finished = True
    
br = 0
while (br != 1):
    screen.fill(COLORS[randint(1, 6)])
    end_surf = pygame.image.load("end.png")
    screen.blit(end_surf, (0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                br=1
                break
        if event.type == pygame.QUIT:
            br=1
            break
    pygame.display.update()

pygame.quit()
