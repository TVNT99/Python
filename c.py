import pygame
import time
import math
pygame.init()
screen = pygame.display.set_mode((500,600))
white= (255,255,255)
black=(0,0,0)
grey = (120,120,120)
running =True 
font = pygame. font.SysFont('sans', 50)
text_1 = font.render('+',True, white)
text_2 = font.render('-', True, white)
text_3 = font.render('+', True, white)
text_4 = font.render('-', True,white)
text_5 = font.render('Start', True, white)
text_6 = font.render('Restart', True, white)
while running:

	screen.fill(white)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	if event.type(mouse_x>= 100 and <=50, mouse_y >=50 and <= 100):
		screen.blit()
	pygame.draw.rect(screen, black, (100,50,50,50))
	pygame.draw.rect(screen, black,(200,50,50,50))
	pygame.draw.rect(screen,black,(100,200,50,50))
	pygame.draw.rect(screen,black,(200,200,50,50))
	pygame.draw.rect(screen,black, (300,50,150,50))
	pygame.draw.rect(screen,black,(300,200,150,50))
	pygame.draw.rect(screen, black, (50,500,400,50))
	pygame.draw.rect(screen,grey,(60,510,380,30))

	pygame.draw.circle(screen,black, (250,380), 80)
	pygame.draw.circle(screen,white,(250,380), 75)
	pygame.draw.circle(screen,black, (250,380), 5)
	pygame.draw.line(screen,black,(250,380),(250,310),2)
	pygame.draw.line(screen,grey,(250,380),(250,350), 5)

	screen.blit(text_1,(120,40))
	screen.blit(text_2,(100,200))
	screen.blit(text_3,(220,40))
	screen.blit(text_4,(200,200))
	screen.blit(text_5,(320,50))
	screen.blit(text_6,(300,200))


	total_secs=0
	mins = int(total_secs/60)
	secs = total_secs - mins*60

	time_now = str(mins) + ":" + str(secs)

	text_time = font.render(time_now, True, black)
	screen.blit(text_time, (120,120))

	x_sec = 250 + 90* math.sin(6*secs * math.pi/180)
	y_sec = 380 - 90* math.cos(6*secs * math.pi/180)
	pygame.draw.line(screen,black,(250,380),(int(x_sec), int(y_sec)),2)

	x_min = 250 +40* math.sin(6 * mins * math.pi/180)
	y_min = 250- 40* math.cos(6* mins * math.pi/180)
	pygame.draw.line(screen, grey,(250,380),(int(x_min), int(y_min)), 5)

	if total != 0:
			pygame draw.rect(screen, white, (60,510, int(380*(total_secs/ total)),30))


	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		pass

	pygame.display.flip()

pygame.quit()