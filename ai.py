from random import randrange
from util import tah

def tah_pocitace(pole, symbol):
	"""Vrátí herní pole se zaznamenaným tahem počítače

	`pole` je herní pole, na které se hraje.
	`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
	nebo za kolečka.

	Strategie: pokud má symbol v poli, pokusit se dát další symbol vedle něj
	Pokud to není možné, randomly vybrat jinou pozici a umístit na ni svůj symbol
	"""
	if '-' not in pole:
		raise ValueError("Pole je plné")
	else:
		if symbol not in pole:
			pozice = randrange(0,20)
			while True:
				if pole[pozice] == "-":
					return tah(pole, pozice, symbol)
				else:
					pozice = randrange(0,20)
		else:
			pozice = pole.index(symbol)
			if pozice == 0:
				if pole[pozice+1] == "-":
					return tah(pole, pozice+1, symbol)
				else:
					pozice = randrange(0,20)
					while True:
						if pole[pozice] == "-":
							return tah(pole, pozice, symbol)
						else:
							pozice = randrange(0,20)
			if pozice == 19:
				if pole[pozice-1] == "-":
					return tah(pole, pozice-1, symbol)
				else:
					pozice = randrange(0,20)
					while True:
						if pole[pozice] == "-":
							return tah(pole, pozice, symbol)
						else:
							pozice = randrange(0,20)

			else:
				if pole[pozice-1] == "-":
					return tah(pole, pozice-1, symbol)
				elif pole[pozice+1] == "-":
					return tah(pole, pozice+1, symbol)
				else:
					pozice = randrange(0,20)
					while True:
						if pole[pozice] == "-":
							return tah(pole, pozice, symbol)
						else:
							pozice = randrange(0,20)


