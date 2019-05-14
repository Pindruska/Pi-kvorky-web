def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """

    if pozice < 0 or pozice > 19:
    	raise ValueError(f'Zadaná pozice není v rozsahu 0-19.')
    elif symbol !="x" and symbol != "o":
    	raise ValueError(f'Symbol musí být x nebo o.')
    elif "-" != pole[pozice]:
    	raise ValueError('Pozice už je obsazená.')
    else:
    	pole_list = list(pole)   #vytvářím z retezce seznam, ktery se snaze meni
    	pole_list[pozice] = symbol
    	pole = ''.join(pole_list)
    	return pole

def vyhodnot(pole):
    """Vrati jednoznakovy retezec podle stavu hry"""
    if 'xxx' in pole:
        return "x"
    elif 'ooo' in pole:
        return "o"
    elif '-' not in pole:
        return "!"
    else:
        return "-"