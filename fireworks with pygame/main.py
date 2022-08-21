import pygame
import time
pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("!! FireWorks !!")

FPS = 60

colors = [
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (0,255,255),
    (255,165,0),
    (255,255,255),
    (230,230,250),
    (255,192,203)
]

class Projectile:
    pass
class Firework:
    pass
class Launcher:
    WIDTH , HEIGHT = 20, 20
    COLOR = 'grey'
    
    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency
        self.start_time = time.time()
        self.fireworks = []
        
    def draw(self,win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))
        
    def loop(self,max_width,max_height):
        current_time = time.time()
        time_elapsed = current_time - self.start_time
        
        def launch(self):
            pass
        
        if time_elapsed * 1000 > self.frequency:
            self.start_time = current_time
            self.launch()
    
    # move all the fireworks 
    
def draw(Launchers):
    win.fill('black')
    
    for launcher in Launchers:
        launcher.draw(win)
        
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    
    launchers = [Launcher(100, HEIGHT - Launcher.HEIGHT, 3000)]
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(launchers)
        
    pygame.quit()
    quit()
if __name__ == '__main__':
    main()