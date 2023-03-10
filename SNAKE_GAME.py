import pygame,random,time
import pygame.mixer

class Snake:
    
    def __init__(self, main_screen, x, y):
        self.main_screen = main_screen
        self.x = x
        self.y = y
        self.length = 1
        self.direction = 'right'
        self.body = [(self.x, self.y)]
        
    def move_snake(self):
        if self.direction == 'right':
            self.x += 20
        elif self.direction == 'left':
            self.x -= 20
        elif self.direction == 'up':
            self.y -= 20
        elif self.direction == 'down':
            self.y += 20
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]
    
    def draw(self):
        snake_image = pygame.image.load('snake.jpg')
        snake_image = pygame.transform.scale(snake_image, (20, 20)).convert()
        for x,y in self.body:
            self.main_screen.blit(snake_image, (x, y))
    
    def grow(self):
        self.length += 1
        
    def check_collisions(self):
        if self.x < 0 or self.x > 780 or self.y < 0 or self.y > 380:
            return True
        for block in self.body[:-1]:
            if self.body[-1] == block:
                return True
        return False
    
class Apple:
    
    def __init__(self, main_screen):
        
        self.main_screen = main_screen
        self.x = random.randint(0, 39) * 20
        self.y = random.randint(0, 19) * 20
    
    def draw(self):
        
        apple_image = pygame.image.load('apple.jpg')
        apple_image = pygame.transform.scale(apple_image, (20, 20))
        apple_image = apple_image.convert()
        self.main_screen.blit(apple_image, (self.x, self.y))

    def check_collision(self, x, y):
        
        if x == self.x and y == self.y:
            return True
        return False
    
def main():
    pygame.init()
    pygame.mixer.init()
    bg_sound=pygame.mixer.Sound('background_music.mp3')
    score_sound=pygame.mixer.Sound('score.mp3')
    game_over_sound=pygame.mixer.Sound('game_over.wav')
    bg_sound.play()

    main_screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Snake Game')

    snake = Snake(main_screen, 400, 200)
    apple = Apple(main_screen)
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 40)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.direction = 'right'
                elif event.key == pygame.K_LEFT:
                    snake.direction = 'left'
                elif event.key == pygame.K_UP:
                    snake.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'down'

        main_screen.fill((200,200,200))
        snake.move_snake()
        snake.draw()
        if apple.check_collision(snake.x, snake.y):
            apple = Apple(main_screen)
            snake.grow()
            score += 20
            score_sound.play()
        apple.draw()
        if snake.check_collisions():
            game_over = font.render("Game Over : Try Again!", True, (10,10,10))
            main_screen.blit(game_over, (250, 200))
            game_over_sound.play()
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
        score_text = font.render("Score: " + str(score), True, (30,0,20))
        main_screen.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(8)

if __name__ == '__main__':
    main()

