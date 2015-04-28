#!/usr/bin/env python
import os
import pygame
import time
import random
import datetime

class pyscope:
	screen = None;
	
	def __init__(self):
		disp_no = os.getenv("DISPLAY")
		if disp_no:
			print "I'm running under X display = {0}".format(disp_no)
		
		drivers = ['fbcon', 'directfb', 'svgalib']
		
		found = False
		
		for driver in drivers:
			if not os.getenv('SDL_VIDEODRIVER'):
				os.putenv('SDL_VIDEODRIVER', driver)
			os.environ["SDL_FBDEV"] = "/dev/fb1"
			try:
				pygame.display.init()
			except pygame.error:
				print 'Driver: {0} failed.'.format(driver)
				continue
			found = True
			break

		if not found:
			raise Exception('No suitable video driver found!')

		size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
		print "Framebuffer size: %d x %d" % (size[0], size[1])
		self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
		self.screen.fill((0, 0, 0,))
		pygame.font.init()
		pygame.display.update()

	def __del__(self):
		"""Shutdown"""

	def test(self):
		red = (255, 0, 0)
		self.screen.fill(red)
		pygame.display.update()

	def run(self):
		for n in range(10):
			self.screen.fill((255, 255, 255))
			pygame.display.update()
			font = pygame.font.Font(None, 50)
			now = datetime.datetime.now()
			time_text = "{0:02d}:{1:02d}:{2:02d}".format(now.hour, now.minute, now.second)
			text = font.render(time_text, 0, (0, 0, 0))
			text_pos = text.get_rect()
			self.screen.blit(text, text_pos)			
			pygame.display.flip()
			time.sleep(1)

scope = pyscope()
scope.run()
