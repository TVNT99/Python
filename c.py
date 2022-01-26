import pygame
import time
import math
pygame.init()
screen = pygame.display.set_mode((500,600))
white= (255,255,255)
black=(0,0,0)
grey = (120,120,120)
red= (255,0,0)
running =True 
clock= pygame.time.Clock()
font = pygame. font.SysFont('sans', 50)
text_1 = font.render('+',True, white)
text_2 = font.render('-', True, white)
text_3 = font.render('+', True, white)
text_4 = font.render('-', True,white)
text_5 = font.render('Start', True, white)
text_6 = font.render('Restart', True, white)
start= False
total_secs=0
total= 0
mins=0
secs=0
while running:
	clock.tick(60)
	screen.fill(white)
	mouse_x, mouse_y=pygame.mouse.get_pos()

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
	

	screen.blit(text_1,(120,40))
	screen.blit(text_2,(100,200))
	screen.blit(text_3,(220,40))
	screen.blit(text_4,(200,200))
	screen.blit(text_5,(320,50))
	screen.blit(text_6,(300,200))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				if(100<mouse_x<150) and (50<mouse_y<100):
					total_secs+=60
					total=total_secs

				if(100<mouse_x<150) and (200<mouse_y<250):
					total_secs-=60	
					total=total_secs

				if(200<mouse_x<250) and (50<mouse_y<100):
					total_secs+=1
					total=total_secs
				if(200<mouse_x<250) and (200<mouse_y<250):
					total_secs-=1
					total=total_secs
				if(200<mouse_x<250) and (50<mouse_y<100):
					total_secs+=1
					total=total_secs
				if(300<mouse_x<450) and (50<mouse_y<100):
					total= total_secs
					start= True
				if(300<mouse_x<450) and(200<mouse_y<250):
					total_secs=0		
			
		
			if total!=0:		
				pygame.draw.rect(screen,red,(60,510,(380*(total_secs/total)),30))
				mins = int(total_secs//60)
				secs = total_secs - mins*60

			

					
				
		mins=total_secs//60
		secs=total_secs-(mins*60)	
		if start:
			if total_secs>0:
				total_secs-= 1
				time.sleep(1) 	
			else: 
				start= False		
		time_now = str(mins) + ":" + str(secs)
		text_time = font.render(time_now, True, black)
		screen.blit(text_time, (140,110))	
		
		x_sec = 250 + 70* math.sin(6*secs * math.pi/180)
		y_sec = 380 - 70* math.cos(6*secs * math.pi/180)
		pygame.draw.line(screen,black,(250,380),(int(x_sec), int(y_sec)),2)

		x_min = 250+40* math.sin(6 * mins * math.pi/180)
		y_min = 380-40* math.cos(6* mins * math.pi/180)
		pygame.draw.line(screen, grey,(250,380),(int(x_min), int(y_min)), 3)
		if total!=0:
			pygame.draw.rect(screen,red,(60,510,int(380*(total_secs/total)),30))
		pygame.display.flip()

pygame.quit()
