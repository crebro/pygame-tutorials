import pygame
import os

width, height = 300, 300
win = pygame.display.set_mode((width, height)) #first arguement is the width and the other is the height
pygame.display.set_caption('My first pygame window') # it takes a string that is going to be the title of your window

class Player:
	def __init__(self, x, y, widthP, heightP):
		self.x = x
		self.y = y
		self.width = widthP
		self.height = heightP
		self.images = self.getImages()
		self.leftImages = self.getleftImages()
		self.imageCounter = 0
		self.leftimageCounter = 0
		self.left = False
		self.right = False

	def getImages(self):
		dirList = os.listdir('Transparent PNG\\03_run')
		giveList = []
		for item in dirList:
			giveList.append(pygame.transform.scale(pygame.image.load(os.path.join('Transparent PNG\\03_run', item)), (self.width, self.height)))

		return giveList

	def getleftImages(self):
		dirList = os.listdir('Transparent PNG\\03_run')
		giveList = []
		for item in dirList:
			giveList.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Transparent PNG\\03_run', item)), (self.width, self.height)), True, False))

		return giveList

	def drawSelf(self, surface):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] and self.x < width - 50:
			self.x += 10
			self.right = True
			self.left = False
			if self.imageCounter == 11:
				self.imageCounter = 0
			self.imageCounter += 1

		if keys[pygame.K_a] and self.x > 0:
			self.x -= 10
			self.right = False
			self.left = True
			if self.leftimageCounter == 12:
				self.leftimageCounter = 0
			self.leftimageCounter += 1

		if self.right:
			win.blit(self.images[self.imageCounter], (self.x, self.y))
		elif self.left:
			win.blit(self.leftImages[self.leftimageCounter], (self.x, self.y))
		else:
			win.blit(self.images[0], (self.x, self.y))



def main():
	background = pygame.image.load('background.png')
	run = True
	red = (255, 0, 0)
	player = Player(0, height-100, 100, 100)
	clock = pygame.time.Clock()
	
	while run:
		clock.tick(60)
		

		win.fill((255, 255, 255))
		win.blit(background, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		player.drawSelf(win)

		


		# pygame.draw.rect(win, red, (x, y, 50, 100)) #the first arguemnt is the window, 2nd is the color, 3d is the rect
		pygame.display.update()

main()
pygame.quit()
