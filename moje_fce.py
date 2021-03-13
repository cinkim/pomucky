import os
from time import asctime
import csv
import requests

def info():
    print("""pristup-načte ze systému win uživatele a aktualni datum a čas,
           funkce přebírá argument 'cesta_logu' pro zápis a údaj zapíše do souboru,
           funkce nic nevrací\n""")
    print()
    print("""vytvor_struktur_adresaru-vytvoří adresářovou strukturu na zadané cestě
            funkce přebírá argument 'folders' což je seznam adresářů v proměnných
            s odkazem na zadanou cestu""")
    print()
    print("""nacti_z_netu-načítá a ukládá soubory z netu pomocí knihovny reguests
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