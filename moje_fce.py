import os
from time import asctime

def info():
    print("""pristup-načte ze systému win uživatele a aktualni datum a čas,
           přebírá argument cesty pro zápis a údaj zapíše do souboru,
           funkce nic nevrací\n""")
    print("""vytvor_struktur_adresaru-vytvoří adresářovou strukturu na zadané cestě""")

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