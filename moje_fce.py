import os
from time import asctime
import csv
import requests

def info():
    print("""pristup/načte ze systému win uživatele a aktualni datum a čas,
           funkce přebírá argument 'cesta_logu' pro zápis a údaj zapíše do souboru,
           funkce nic nevrací\n""")
    print()
    print("""vytvor_struktur_adresaru/vytvoří adresářovou strukturu na zadané cestě
            funkce přebírá argument 'folders' což je seznam adresářů v proměnných
            s odkazem na zadanou cestu""")
    print()
    print("""nacti_z_netu/načítá a ukládá soubory z netu pomocí knihovny reguests
           funkce má 2 argumenty 'url' a 'vystup' což jsou vstupní a výstupní cesty""")

def nacti_z_netu(url, vystup):
    r = requests.get(url, allow_redirects=True)
    open(vystup, 'wb').write(r.content)

def pristup(self, cesta_logu):
    """načte uživatele, datum a čas-udaje zapíše do souboru"""
    self.uzivatel = os.getenv('username') # načtení uživatele
    self.datum_cas = asctime()   #  načtení aktuálního data a času
    self.log = self.datum_cas + " " + self.uzivatel
    try:
        with open(cesta_logu, mode="a", encoding="UTF-8") as pr:
            print(self.log, file=pr)
    except FileNotFoundError:
        return


def vytvor_struktur_adresaru(folders):
    """DATABASE_FOLDER = './.database/'
    DOWNLOAD_FOLDER = './.download/'
    DATASETS_FOLDER = './.datasets/'
    EXPORTS_FOLDER = './.exports/'

    WORKING_FOLDERS = [
                        DATABASE_FOLDER,
                        DOWNLOAD_FOLDER,
                        DATASETS_FOLDER,
                        EXPORTS_FOLDER,
                    ]"""
    # příklad pro zadání cest a adresářů
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
			
def datum():
	"""
	import datetime
	import time
	Funkce vrátí seznam datumů od zadaného počátku až do včerejšího datumu
	"""
    while True:
        r = int(input("Zadej počáteční rok hledání: "))
        m = int(input("Zadej počáteční měsíc hledání: "))
        d = int(input("Zadej počáteční den hledání: "))
        print("Vytvářím seznam datumů")
        seznam_datumu = []
        akt_time = time.strftime("%Y %m %d", time.localtime())
        akt_time = akt_time.replace(" ", "-")
        while True:
            try:
                dat = datetime.date(r, m, d)
                dat = str(dat)
                if dat == akt_time:
                    return seznam_datumu
                elif dat > akt_time:
                    print("Nemám křišťálovou kouli.")
                    break
                seznam_datumu.append(dat)
                d +=1
            except ValueError:
                if m == 2 and d > 28:
                    m = 3
                    d = 1
                elif m != 2 and m != 12:
                    m +=1
                    d = 1
                elif m == 12:
                    r +=1
                    m = 1
                    d = 1