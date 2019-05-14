"""
from flask import Flask, render_template, request
from ai import tah_pocitace
from util import tah

app = Flask(__name__) #magic aby to fungovalo

@app.route('/') #pokracovani magic - zadavame adresu stranky, musi byt radek nad tou funkci
def hra():
	pole = request.args.get('pole')

	if not pole:	#pokud jeste nemam pole
		pole = '-' * 20

	muj_tah = request.args.get('cislo') #args je slovnik
	if muj_tah:
		pole = tah(pole, int(muj_tah), 'o')

	pole = tah_pocitace(pole, 'x')

	ocislovane_pole = enumerate(pole) #projede pole a vrati dvojici - poradove cislo a hodnota

	return render_template('hra.html', pole=pole, ocislovane_pole=ocislovane_pole, cislo=muj_tah) 

	#jmeno - jmeno argumentu, #hodnota
"""
from flask import Flask, render_template, request

from util import tah, vyhodnot
from ai import tah_pocitace

app = Flask(__name__)

@app.route('/')
def hra():
    if 'pole' in request.args:
        pole = request.args['pole']
    else:
        pole = '-' * 20
    if 'cislo' in request.args:
        cislo_policka = int(request.args['cislo'])
        pole = tah(pole, cislo_policka, 'x')
        vyhodnot(pole)
        pole = tah_pocitace(pole, 'o')
        vyhodnot(pole)

    return render_template(
        'hra.html',
        ocislovane_pole=enumerate(pole),
        pole=pole,
    )