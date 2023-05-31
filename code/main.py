import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption('Croco Valley')
		self.clock = pygame.time.Clock()
		self.level = Level()
		
		self.loop = True

		#janelas
		self.window_init = pygame.image.load('../assets/valley.png').convert_alpha()
		self.window_end = pygame.image.load('../assets/play.png').convert_alpha()
		self.window_manual = pygame.image.load('../assets/jogadas.png').convert_alpha()

		
		self.state = INIT1

	def init_screen(self):
		print('Entrou no init')
		while self.loop:
			# ----- Trata eventos
			for event in pygame.event.get():
				# ----- Verifica consequências
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.state = INIT2
						self.loop = False
				if event.type == pygame.QUIT:
					pygame.quit()
					self.state = QUIT

			self.screen.blit(self.window_init, self.screen_rect)
			pygame.display.update()
		self.loop = True
		return self.state
	
	def manual_screen(self):
		while self.loop:
			# ----- Trata eventos
			for event in pygame.event.get():
				# ----- Verifica consequências
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.state = GAME
						self.loop = False
				if event.type == pygame.QUIT:
					pygame.quit()
					self.state = QUIT

			self.screen.blit(self.window_init,(0,0))
			pygame.display.update()
		self.loop = True
		return self.state

	def run(self):
		while True: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			dt = self.clock.tick() / 1000
			self.level.run(dt)  
			pygame.display.update()

		# self.loop = True
		# return self.state
	
	def rodar(self):
		JOG =True
		while JOG: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					print("jogo")
					JOG = False
			self.screen.blit(self.window_init, self.screen_rect)
			# dt = self.clock.tick() / 1000
			# self.level.run(dt)  
			pygame.display.update()

	
	def main():
		game = Game()
		state = INIT1
		print('Chamando')
		while True:
			print(state)
			if state == INIT1:
				state = game.init_screen()
			elif state == INIT2:
				state = game.manual_screen()
			elif state == GAME:
				state = game.run()
			elif state == QUIT:
				break
if __name__== '__main__':
	game = Game()
	game.rodar()
	game.run()