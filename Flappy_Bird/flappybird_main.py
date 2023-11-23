import pygame
import sys
import random
from flappybird_modules.flappybird_bird import Bird
from flappybird_modules.flappybird_pipe import Pipe
from flappybird_modules.flappybird_button import Button

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 512)
pygame.init()
clock = pygame.time.Clock()

def main():
	screen_width = 864
	screen_height = 650

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Flappy Bird')

	#define font
	font = pygame.font.Font('flappybird_font.ttf', 60)
	font2 = pygame.font.Font('flappybird_font.ttf', 55)

	#define game variables
	ground_scroll = 0

	flying = False
	game_over = False
	stop_blit_begin = False

	pipe_freq = 1500 #milliseconds
	last_pipe = pygame.time.get_ticks() - pipe_freq 
	pass_pipe = False

	score = 0
	high_score = 0

	#define sound
	flap_sound = pygame.mixer.Sound("flappybird_sound/sound_wing.wav")
	hit_sound = pygame.mixer.Sound("flappybird_sound/sound_hit.wav")
	score_sound = pygame.mixer.Sound("flappybird_sound/sound_point.wav")
	collision_sound_played = False

	#load images
	bg = pygame.image.load("flappybird_images/bg.png").convert()
	ground = pygame.image.load("flappybird_images/ground.png").convert()
	button = pygame.image.load('flappybird_images/restart.png').convert_alpha()
	game_over_img = pygame.transform.scale(pygame.image.load('flappybird_images/gameover.png').convert_alpha(), (360, 110))
	game_over_rect = game_over_img.get_rect(center = (screen_width // 2 + 10, screen_height // 2 - 100))
	message = pygame.image.load('flappybird_images/begin.png').convert_alpha()
	message_rect = message.get_rect(center = (screen_width // 2, screen_height // 2))

	#function for outputting text onto the screen
	def draw_text(text, font, text_col, x, y):
		text = font.render(text, True, text_col)
		text_rect = text.get_rect(center = (x, y))
		screen.blit(text, text_rect)

	def reset_game():
		pipe_group.empty()
		flappy.rect.x = 100
		flappy.rect.y = screen_height // 2
		score = 0
		return score

	#function to check high score
	def update_score(score, high_score):
		if score > high_score:
			high_score = score
		return high_score	

	pipe_group = pygame.sprite.Group()
	bird_group = pygame.sprite.Group()
	flappy = Bird(100, screen_height // 2 - 25)
	bird_group.add(flappy)

	#create restart button instance
	button = Button(screen_width // 2 - 60, screen_height // 2, button, screen)

	while True:
		clock.tick(60)

		#draw background, bird and pipe
		screen.blit(bg, (0,0))

		pipe_group.draw(screen)
		bird_group.draw(screen)
		bird_group.update(flying, game_over, flap_sound)

		#draw and scroll the ground
		screen.blit(ground, (ground_scroll, 550))

		#draw the beginning image
		if stop_blit_begin == False:
			screen.blit(message, message_rect)

		#check the score
		if len(pipe_group) > 0:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
				and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
				and pass_pipe == False:
				pass_pipe = True
			if pass_pipe == True:
				if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
					score_sound.play()
					score += 1
					pass_pipe = False
		draw_text(str(score), font, 'white', screen_width // 2, 70)

		#look for collision 
		if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0: #False parts prevent the bird & pipes being killed if colliding
			game_over = True
			if collision_sound_played == False:
				hit_sound.play()
				collision_sound_played = True
		if flappy.rect.bottom >= 550:
			if collision_sound_played == False:
				hit_sound.play()
				collision_sound_played = True
			game_over = True
			flying = False

		if flying == True and game_over == False:
			#generate new pipes
			time_now = pygame.time.get_ticks()
			if time_now - last_pipe > pipe_freq:
				pipe_height = random.choice([-200, -175, -150, -125, -100, -75, -50, -25, 0, 25, 50, 75, 100])
				btm_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, -1)
				top_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, 1)
				pipe_group.add(btm_pipe)
				pipe_group.add(top_pipe)
				last_pipe = time_now

			pipe_group.update()

			ground_scroll -= 4
			if abs(ground_scroll) > 35:
				ground_scroll = 0

		#check for game over and reset
		if game_over:
			high_score = update_score(score, high_score)
			draw_text(f'High Score: {high_score}', font2, 'chocolate1', screen_width // 2 , screen_height // 2 + 100)
			screen.blit(game_over_img, game_over_rect)
			if button.draw():
				game_over = False
				score = reset_game()
				collision_sound_played = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
				stop_blit_begin = True
				flying = True

		pygame.display.update()

if __name__ == '__main__':
	main()
