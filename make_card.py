from PIL import Image, ImageDraw, ImageFont, ImageFilter
from config import Config
import sys

font_type = ImageFont.truetype(Config.FONT_FACE, Config.FONT_SIZE)

if __name__=='__main__':
	if len(sys.argv) < 3:
		print('Pass a template file and an input string')
		exit()

	template = Image.open(sys.argv[1])
	full_name = [i.strip().upper() for i in sys.argv[3].split(' ')]
	phone = [i for i in sys.argv[4] if i in '0123456789']
	try:
		phone = f'+7-({phone[-10]}{phone[-9]}{phone[-8]})-{phone[-7]}{phone[-6]}{phone[-5]}-{phone[-4]}{phone[-3]}-{phone[-2]}{phone[-1]}'
	except:
		print('Pass a right phone number specified')
		exit()
		
	ln = max([len(i) for i in full_name])
	
	drawer = ImageDraw.Draw(template)
	orientation = Config.TEXT_ORIENTATION
	orientation[0] -= Config.LETTER_SIZE * ln

	for word in full_name:
		drawer.text(orientation, word, font=font_type, fill=Config.TEXT_COLOR_NORMAL, stroke_width=Config.FONT_WIDTH_NORMAL)
		orientation[1] += Config.TEXT_SPACING
	
	orientation = Config.PHONE_ORIENTATION
	drawer.text(orientation, phone, font=font_type, fill=Config.TEXT_COLOR_NORMAL, stroke_width=Config.FONT_WIDTH_NORMAL)
	
	template.save(sys.argv[2])
