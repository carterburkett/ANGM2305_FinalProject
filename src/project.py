import pygame
import random

pygame.init()
font20 = pygame.font.SysFont('arial', 40)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock() 
FPS = 60

class Paddle:
	def __init__(self, posx, posy, width, height, speed, color, hitColor):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		self.hitColor = hitColor
		self.yDir = 0
		self.xDir = 0
		self.collided = False
		self.rect = pygame.Rect(posx, posy, width, height)
		self.rectOut = pygame.draw.rect(screen, self.color, self.rect)

	def display(self):
		self.rectOut = pygame.draw.rect(screen, self.color, self.rect)

	def update(self, yFac):
		self.posy = self.posy + self.speed * yFac

		if self.posy <= 0:
			self.posy = 0
		elif self.posy + self.height >= HEIGHT:
			self.posy = HEIGHT-self.height
		
		self.rect = (self.posx, self.posy, self.width, self.height)

	def displayScore(self, text, score, x, y, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)
		screen.blit(text, textRect)

	def displayEndScreen(self, text, score, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (WIDTH/2, HEIGHT/2)
		screen.blit(text, textRect)

	def getRect(self):
		return self.rect

	def hit(self):
		self.collided = True

class Ball:
	def __init__(self, posx, posy, radius, speed, color):
		self.posx = posx
		self.posy = posy
		self.radius = radius
		self.speed = speed
		self.minSpeed = speed
		self.velMod = 1
		self.color = color
		spawnDir = [-1, 1]
		self.xDir = random.choice(spawnDir)
		self.yDir = random.choice(spawnDir)
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)
		self.newBall = 1

	def display(self):
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)

	def update(self):
		self.posx += self.speed * self.xDir
		self.posy += self.speed * self.yDir

		if self.posy <= 0 or self.posy >= HEIGHT:
			self.yDir *= -1

		if self.posx <= 0 and self.newBall:
			self.newBall = 0
			return 1
		elif self.posx >= WIDTH and self.newBall:
			self.newBall = 0
			return -1
		else:
			return 0

	def increaseVel(self, mod):
		self.speed *= mod
		self.speed = pygame.math.clamp(self.speed, self.minSpeed, self.minSpeed * 2)

	def reset(self):
		self.posx = WIDTH//2
		self.posy = HEIGHT//2
		spawnDir = [-1, 1]
		self.xDir *= random.choice(spawnDir)
		self.newBall = 1

	def hit(self):
		self.xDir *= -1

	def getXDir(self):
		return self.xDir
	
	def getYDir(self):
		return self.yDir

	def getRect(self):
		return self.ball
	
	def getNextRect(self):
		nextBall = self.ball
		nextBall.center = (self.ball.centerx + (self.xDir), self.ball.centery + (self.yDir))
		return nextBall

class AIManager:
	def __init__(self, paddle):
		self.paddle = paddle
		self.difficulty = 0
		self.active = False
		self.score = 0
		self.playerScore = 0

	def update(self, paddle, ball):
		if ball.getXDir() == 1:
			if (paddle.posy + paddle.height/2) > ball.posy:
				paddle.update(-1)

			elif (paddle.posy + paddle.height/2) < ball.posy:
				paddle.update(1)

	
	def increaseDifficulty(self, paddle, playerRef):
		if(self.playerScore - self.score >= 3 and self.playerScore != playerRef and self.playerScore % 2 == 0):
			paddle.speed += 3

def main():
	running = True

	player = Paddle(20, HEIGHT/2 - 50, 10, 100, 14, WHITE, BLUE)
	aiPaddle = Paddle(WIDTH-30, HEIGHT/2 - 50, 10, 100, 8, WHITE, RED)
	ball = Ball(WIDTH//2, HEIGHT//2, 7, 12, WHITE)
	aiComp = AIManager(aiPaddle)

	paddles = [player, aiPaddle]

	playerScore, aiScore = 0, 0
	player.yDir, aiPaddle.yDir = 0, 0

	while running:
		screen.fill(BLACK)
		for event in pygame.event.get():
			aiPaddle.speed += aiComp.difficulty
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					player.yDir = -1
				if event.key == pygame.K_s:
					player.yDir = 1
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				if event.key == pygame.K_SPACE:
					playerScore = 0
					aiScore = 0

					player = Paddle(20, 0, 10, 100, 10, WHITE, BLUE)
					aiPaddle = Paddle(WIDTH-30, 0, 10, 100, 4, WHITE, RED)
					ball = Ball(WIDTH//2, HEIGHT//2, 7, 12, WHITE)
					aiComp = AIManager(aiPaddle)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					aiPaddle.yDir = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					player.yDir = 0

		for paddle in paddles:
			if pygame.Rect.colliderect(ball.getNextRect(), paddle.getRect()) or pygame.Rect.colliderect(ball.getRect(), paddle.getRect()):
				ball.hit()
				paddle.hit()
				if ball.getYDir == player.yDir:
					ball.increaseVel(1.25)
					print("Ball Speed = " + str(ball.speed))

		player.update(player.yDir)
		aiComp.update(aiPaddle, ball)
		
		

		if(playerScore <= 3 and aiScore <= 3):
			point = ball.update()

			if point == -1:
				passRef = playerScore
				playerScore += 1
				aiComp.playerScore = playerScore
				aiComp.increaseDifficulty(aiPaddle, passRef)
			elif point == 1:
				aiScore += 1
				aiComp.score = aiScore

			if point: 
				ball.reset()


			player.display()
			aiPaddle.display()
			ball.display()

			player.displayScore("Player:", 
							playerScore, 150, 30, WHITE)
			aiPaddle.displayScore("AI: ", 
							aiScore, WIDTH-150, 30, WHITE)
		else:
			if(playerScore > aiScore):
				player.displayEndScreen("Press Space to Play Again! You Win! Your Score Was: ", playerScore, BLUE)
			elif(aiScore > playerScore):
				aiPaddle.displayEndScreen("You Lose! Press Space to play again! Your Score Was: ", playerScore, RED)

		pygame.display.update()
		clock.tick(FPS)	 


if __name__ == "__main__":
	main()
	pygame.quit()
