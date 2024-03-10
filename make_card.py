from PIL import Image, ImageDraw, ImageFont, ImageFilter
from config import Config
import sys

font_type = ImageFont.truetype(Config.FONT_FACE, Config.FONT_SIZE)

if __name__=='__main__':
	if len(sys.argv) < 3:
		print('Run with a template file and an input string')
		exit()

	template = Image.open(sys.argv[1])
	full_name = [i.strip().upper() for i in sys.argv[3].split(' ')]
	
	drawer = ImageDraw.Draw(template)
	orientation = Config.TEXT_ORIENTATION
	for word in full_name:
		drawer.text(orientation, word, font=font_type, fill=Config.TEXT_COLOR_NORMAL, stroke_width=Config.FONT_WIDTH_NORMAL)
		orientation[1] += Config.TEXT_SPACING
	
	template.save(sys.argv[2])
