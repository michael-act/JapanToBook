from .settings import IMAGES_PATH, FONTS_PATH

import random
from datetime import date
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

IMAGES_PATH = IMAGES_PATH
FONTS_PATH = FONTS_PATH

IMAGES = ['Middle Page.jpg', 'Last Page.jpg']
FONTS = ['AsobiMemogaki-Regular-1-01.ttf', 'ShigotoMemogaki-Regular-1-01.ttf', 'éªéFÄÜ.otf']

class WriteBox:
	def __init__(self, color='rgb(103, 99, 109)'):
		self.colorFont = color

	def random_font(self, size):
		'''
		Return: name of random choices font.
		'''

		which_font = random.choice(FONTS)
		font = ImageFont.truetype(FONTS_PATH+which_font, size=size)
		return font


	def midBook1(self, char1, char2=''):
		'''
		Return: Written japan character image of Middle Book
		'''

		self.writer = 'midBook1'
		self.image = Image.open(IMAGES_PATH+IMAGES[0])

		sizeFont = 120

		draw = ImageDraw.Draw(self.image)
		for htl in range(18):
			y_ = 120 * htl
			if 5 < htl < 12:
			    y_ += 20
			elif htl < 15:
			    y_ += 25
			else:
			    y_ += 30

			for vtl in range(14):
				x_ = 120 * vtl
				x_ -= 10 if (htl > 5) else 0

				(x1, y1) = (260+x_, 350+y_)
				(x2, y2) = (2195+x_, 360+y_)

				# Draw a Japan character
				draw.text((x1, y1), char1, fill=self.colorFont, font=self.random_font(sizeFont))
				draw.text((x2, y2), char2, fill=self.colorFont, font=self.random_font(sizeFont))

		return self.saveFile()


	def lstBook1(self, char1):
		'''
		Return: Written japan character image of Last Book
		'''

		self.writer = 'lstBook1'
		self.image = Image.open(IMAGES_PATH+IMAGES[1])

		sizeFont = 155

		draw = ImageDraw.Draw(self.image)
		for htl in range(18):
			y_ = 185 * htl
			y_ -= 15 if (htl >= 15) else 0

			for vtl in range(14):
				x_ = 190 * vtl
				x_ -= 5 if htl >= 15 else 0

				(x, y) = (205+x_, 335+y_)

				# Draw a Japan character
				draw.text((x, y), char1, fill=self.colorFont, font=self.random_font(sizeFont))

		return self.saveFile()


	def saveFile(self):
		'''
		Return: Name of exported written japan file
		'''

		now = datetime.now()
		day = ['Mon','Tues','Wed','Thurs','Fri','Satur','Sun'][date.weekday(now)]
		name_file = f"{day}-{now.strftime('%Y-%m %H-%M-%S')}.jpg"
		self.image.save(IMAGES_PATH+name_file, 'JPEG')
		return name_file

if __name__ == '__main__':
	IMAGES_PATH = 'images/' 
	FONTS_PATH = 'fonts/'
	# <Code Here if you want to run this script only>
