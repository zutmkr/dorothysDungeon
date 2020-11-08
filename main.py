# -*- coding: utf-8 -*-
import os
import os.path
import sys
import pickle
import Undergrounds
import Members
import Functions
import platform
from generator_map import generator, mapsgen
from Draw_Images import rysuj, rysuj_oddo
from config import Version


PIK = "save/objects.bj"

os.system('mode con: cols=115 lines=55')


def menu_glowne():
    od = 0
    do = 5  
    
    while True:
        Functions.clear_screen()  # czyszczenie ekranu
        rysuj("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        rysuj("lang/PL/menu_glowne_instrukcje.txt")
        rysuj_oddo("lang/PL/menu_glowne.txt",od,do)
        
        inp = input()
        if inp == 'w' and od >= 6:
            od -= 6
            do -= 6
        elif inp == 's' and od >= 0 and do < 23:
            od += 6
            do += 6
        elif inp == 'k':
            if od >=0 and do <=6:
                nowa_gra()
            elif od >=6 and do <=12:
                wczytaj_gre()
            elif od >=12 and do <=18:
                extra()
            elif od >=18 and do <=24:
                wyjdz_z_gry()
   
   
def nowa_gra(poziom_pgen = None, wielkosc_mapygen = None, points_zycia = None, sila = None):
    gr = Members.Player()
    while gr.name == '':
        gr.name = input("\n\tENTER HERO NAME\n\t")
        if len(gr.name) > 9:
            print('NAME TOO LONG. MAX 9 CHARS')
            gr.name = ''
    Functions.status = ''

    if poziom_pgen is not None or wielkosc_mapygen is not None or points_zycia is not None:
        Undergrounds.poziom_p = poziom_pgen.get()
        maps = mapsgen
        gr.pz = points_zycia.get()
        gr.s = sila.get()
    else:
        Undergrounds.poziom_p = 1
        maps = Undergrounds.Mapa()
        maps.przygotuj_mape()

    maps.mapa[0][0] = gr
    gr.take_position(maps)
    Functions.widocznosc(gr, maps)
    maps.rysuj_mape()
    Functions.poruszanie_po_mapie(gr, maps)

    
def wczytaj_gre():
    if (os.path.exists(PIK)):
      data2 = []
      gr = Members.Player()
      maps = Undergrounds.Mapa()

      with open(PIK, "rb") as f:
        for _ in range(pickle.load(f)):
            data2.append(pickle.load(f))
            gr = data2[0]
            maps = data2[1]
            Undergrounds.poziom_p = data2[2]
            gr.list_of_item = data2[3]
            gr.tasks = data2[4]
            
            if gr.name == '':
                gr.name = input("ENTER HERO NAME\n\t")
            
            gr.take_position(maps)
            maps.rysuj_mape()
            Functions.poruszanie_po_mapie(gr, maps)
    else:
      Functions.clear_screen()
      rysuj("static/error_msg/load_save_error")
      Functions.get_char(False)
      return

    
def wyjdz_z_gry():
    sys.exit(0)

    
def extra():
    od = 24
    do = 28  
    
    while True:
        Functions.clear_screen()  # czyszczenie ekranu
        rysuj("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        rysuj("lang/PL/menu_glowne_instrukcje.txt")
        rysuj_oddo("lang/PL/menu_glowne.txt",od,do)
        inp = input()
        if inp == 'w' and od >= 28:
            od -= 5
            do -= 5
        elif inp == 's' and od >= 24 and do < 37:
            od += 5
            do += 5
        elif inp == 'k':
            if od >=24 and do <=28:
                generator()
            elif od >=28 and do <=34:
                opcje()
            elif od >=34 and do <=39:
                menu_glowne()
                
def opcje():
    od = 39
    do = 43  
      
    while True:
        Functions.clear_screen()  # czyszczenie ekranu
        rysuj("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        rysuj("lang/PL/menu_glowne_instrukcje.txt")
        rysuj_oddo("lang/PL/menu_glowne.txt",od,do)
        inp = input()
        if inp == 'w' and od >= 43:
            od -= 5
            do -= 5
        elif inp == 's' and od >= 39 and do < 52:
            od += 5
            do += 5
        elif inp == 'k':
            if od >=39 and do <=43:
                Functions.get_char()
            elif od >=43 and do <=48:
                Functions.clear_screen()  # czyszczenie ekranu
                rysuj("static/O_GRZE.txt")
                return False
            elif od >=48 and do <=54:
                extra()
    
if __name__ == "__main__":
    menu_glowne()
