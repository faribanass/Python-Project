import pygame
from settings import *
from snake import Snake
from food import Food
from highscore import load_highscore, save_highscore

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.state = "MENU"
        self.difficulty = "MEDIUM"
        self.fps = DIFFICULTY_LEVELS[self.difficulty]

        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.highscore = load_highscore()

        self.font = pygame.font.SysFont("arial", 40)

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        if self.state == "PLAYING":
            self.snake.move()

            if self.snake.body[0] == self.food.position:
                self.snake.grow = True
                self.food = Food()
                self.score += 1

            if self.snake.check_collision():
                if self.score > self.highscore:
                    save_highscore(self.score)
                self.state = "GAME_OVER"

    def draw(self):
        self.screen.fill(BLACK)

        if self.state == "MENU":
            self.draw_menu()

        elif self.state == "PLAYING":
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (20,20))

        elif self.state == "GAME_OVER":
            over = self.font.render("GAME OVER", True, RED)
            self.screen.blit(over, (WIDTH//2 - 120, HEIGHT//2 - 40))

        pygame.display.update()

    def draw_menu(self):
        title = self.font.render("SNAKE GAME", True, GREEN)
        start = self.font.render("Press SPACE to Start", True, WHITE)

        self.screen.blit(title, (WIDTH//2 - 150, HEIGHT//2 - 80))
        self.screen.blit(start, (WIDTH//2 - 200, HEIGHT//2))

    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.state == "MENU" and event.key == pygame.K_SPACE:
                        self.state = "PLAYING"

                    elif self.state == "GAME_OVER" and event.key == pygame.K_r:
                        self.reset()
                        self.state = "MENU"

                    elif self.state == "PLAYING":
                        if event.key == pygame.K_UP:
                            self.snake.change_direction(0,-1)
                        if event.key == pygame.K_DOWN:
                            self.snake.change_direction(0,1)
                        if event.key == pygame.K_LEFT:
                            self.snake.change_direction(-1,0)
                        if event.key == pygame.K_RIGHT:
                            self.snake.change_direction(1,0)

            self.update()
            self.draw()

        pygame.quit()