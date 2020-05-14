from phue import Bridge
import sys
import time
import random

colours = {}
colours['red'] = (65535, 254)
colours['white'] = (0, 0)
colours['orange'] = (8000, 254)
colours['yellow'] = (13000, 254)
colours['green'] = (24000, 254)
colours['aqua'] = (36000, 254)
colours['blue'] = (40000, 254)
colours['dark blue'] = (46000, 254)
colours['purple'] = (49000, 254)
colours['pink'] = (60000, 254)

def connect_to_bridge():
	b = Bridge('192.168.1.65')
	lights = b.get_light_objects('name')
	for light in lights:
		print(light)
	return lights


def living_room_lights(colour, brightness):
	lights = connect_to_bridge()
	for light in lights:
		if light == 'Hue color lamp 2' or light == 'Hue color lamp 3' or light == 'Hue lightstrip plus 1':
			lights[light].on = True
			lights[light].hue = colours[colour][0]
			lights[light].saturation = colours[colour][1]
			lights[light].brightness = brightness

def disco():
	lights = connect_to_bridge()
	while True:
		for key in colours:
			for light in ['Hue color lamp 2', 'Hue color lamp 3', 'Hue lightstrip plus 1']:
				lights[light].on = True
				lights[light].hue = colours[key][0]
				lights[light].saturation = colours[key][1]
				lights[light].brightness = random.randint(0, 254)

def error_check():
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			if sys.argv[1] == 'disco':
				disco()
			elif sys.argv[1] not in colours:
				return False
			else:
				colour = sys.argv[1]
		elif len(sys.argv) == 3:
			if sys.argv[1] not in colours or not sys.argv[2].isnumeric() or int(sys.argv[2]) > 100 or int(sys.argv[2]) < 0:
				return False
			else:
				colour = sys.argv[1]
				brightness = brightness * int(sys.argv[2])/100
		elif len(sys.argv) > 3:
			return False
	return True

if __name__ == '__main__':
	err = "usage: python3 hueproject.py red|white|orange|yellow|green|aqua|blue|dark blue|purple|pink 0-100"
	colour = 'white'
	brightness = 254

	if not error_check():
		print(err)
		sys.exit()


	living_room_lights(colour, int(brightness))