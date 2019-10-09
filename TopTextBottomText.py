import os, random
from PIL import Image, ImageDraw, ImageFont

def Meme(background, top, bottom):
	image = Image.open(background)
	width, height = image.size
	draw = ImageDraw.Draw(image)
	def topText(message):
		message = message.upper()
		x = 0
		y = 0
		point = round((width*height)**(1/2))
		while(True):
			font = ImageFont.truetype('impact.ttf', point)
			textWidth, textHeight = draw.textsize(message, font=font)
			x = (width-textWidth)/2
			y = 0
			if (textWidth <= 0.95*width)and(textHeight <= height/4):
				break
			else:
				point = point - 1
		outlineFactor = round(point/16)
		for i in range(outlineFactor):
			draw.text((x-i, y), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x-i, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x-i, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
		draw.text(xy=(x, y), text=message, fill='rgb(255, 255, 255)', font=font)
	def bottomText(message):
		message = message.upper()
		x = 0
		y = 0
		point = width
		while(True):
			font = ImageFont.truetype('impact.ttf', point)
			textWidth, textHeight = draw.textsize(message, font=font)
			x = (width-textWidth)/2
			y = 0.95*(height-textHeight)
			if (textWidth <= 0.95*width)and(textHeight <= height/4):
				break
			else:
				point = point - 1
		outlineFactor = round(point/16)
		for i in range(outlineFactor):
			draw.text((x-i, y), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x-i, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y+i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x-i, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
			draw.text((x+i, y-i), text=message, font=font, fill='rgb(0, 0, 0)')
		draw.text(xy=(x, y), text=message, fill='rgb(255, 255, 255)', font=font)
	topText(top)
	bottomText(bottom)
	image.save('freshmeme.png')
def randomMeme(directory, top, bottom):
	choice = directory + '/' + random.choice(os.listdir(directory))
	Meme(choice, top, bottom)