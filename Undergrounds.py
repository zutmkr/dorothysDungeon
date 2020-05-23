
# -*- coding: utf-8 -*-
import random
import os
import Draw_Images
import Room
import Functions
import pole


ile_map = 0
poziom_p = 1
rodzaj_mapy = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0]]
prawda_falsz = [True, False]



class Mapa():
    def __init__(self, wielkosc_mapygen = None):
        global ile_map
        global wybrana

        # tworzenie mapy gry
        if wielkosc_mapygen is not None:
            wielkosc_mapy = [0] * wielkosc_mapygen.get()
        else:
            wielkosc_mapy = [0] * random.randint(7, 14)

        wybrana = wielkosc_mapy
        self.mapa = []  # ATR: MAPA
        for i in range(len(wielkosc_mapy)): self.mapa.append(wielkosc_mapy[:])
        
        self.list_of_item_pokoi = [Room.Pokoj() for i in range(len(wielkosc_mapy) ** 2)]  # ATR: list_of_item_POKOI
        k = 0
        for i in range(len(wielkosc_mapy)):
            for j in range(len(wielkosc_mapy)):
                self.mapa[i][j] = self.list_of_item_pokoi[k]
                if random.choice(prawda_falsz):
                    self.mapa[i][j].otwarty = True
                    if random.choice(prawda_falsz):
                        self.mapa[i][j].event = True
                else:
                    self.mapa[i][j].otwarty = False
                k += 1
        self.mapa[len(wielkosc_mapy)-1][len(wielkosc_mapy)-1].otwarty = True

    def przygotuj_mape(self, wielkosc_mapygen = None):
        global ile_map
        global wybrana
        wielkosc_mapy = wybrana #random.choice(rodzaj_mapy)
        list_of_item_otwarta = []
        list_of_item_zamknieta = []
        nowa_mapa = []
        znaleziony = 0
        mapa_ok = 0
        ile_map = 0
        
        for i in range(len(wielkosc_mapy)): nowa_mapa.append(wielkosc_mapy[:])

        for i in range(len(wielkosc_mapy)):
            for j in range(len(wielkosc_mapy)):
                nowa_mapa[i][j] = pole.Pole(i,j,self.mapa[i][j].otwarty)
        
        nowa_mapa[0][0].aktualny = True
        nowa_mapa[0][0].otwarty = True
        nowa_mapa[0][0].h = 10 * (abs(nowa_mapa[0][0].x - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].x) + abs(nowa_mapa[0][0].y - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].y))
        nowa_mapa[0][0].suma = nowa_mapa[0][0].g + nowa_mapa[0][0].h
        list_of_item_otwarta.append(nowa_mapa[0][0])
        while True:
            #print(list_of_item_otwarta)
            for Pole in list_of_item_otwarta:
                if Pole.x == (len(wielkosc_mapy) - 1) and Pole.y == (len(wielkosc_mapy) - 1):
                    mapa_ok = 1
            if not list_of_item_otwarta:
                if wielkosc_mapygen is not None:
                    self.__init__(wielkosc_mapygen)
                else:
                    self.__init__()
                ile_map += 1
                wielkosc_mapy = wybrana
                list_of_item_otwarta = []
                list_of_item_zamknieta = []
                nowa_mapa = []
                znaleziony = 0
                mapa_ok = 0

                for i in range(len(wielkosc_mapy)): nowa_mapa.append(wielkosc_mapy[:])

                for i in range(len(wielkosc_mapy)):
                    for j in range(len(wielkosc_mapy)):
                        nowa_mapa[i][j] = pole.Pole(i,j,self.mapa[i][j].otwarty)
                nowa_mapa[0][0].aktualny = True
                nowa_mapa[0][0].otwarty = True
                nowa_mapa[0][0].h = 10 * (abs(nowa_mapa[0][0].x - nowa_mapa[len(wielkosc_mapy)- 1][len(wielkosc_mapy)- 1].x) + abs(nowa_mapa[0][0].y - nowa_mapa[len(wielkosc_mapy)- 1][len(wielkosc_mapy)- 1].y))
                nowa_mapa[0][0].suma = nowa_mapa[0][0].g + nowa_mapa[0][0].h
                list_of_item_otwarta.append(nowa_mapa[0][0])
            
            aktualny = min(list_of_item_otwarta, key=lambda Pole: Pole.suma)
            try:
                for Pole in list_of_item_zamknieta:
                    if Pole == nowa_mapa[aktualny.x+1][aktualny.y]:
                        znaleziony = 1
                        break
                    else:
                        znaleziony = 0
                if nowa_mapa[aktualny.x+1][aktualny.y].otwarty and znaleziony == 0:
                    nowa_mapa[aktualny.x+1][aktualny.y].g = 10 * (nowa_mapa[aktualny.x+1][aktualny.y].x + (nowa_mapa[aktualny.x+1][aktualny.y].y - 1))
                    nowa_mapa[aktualny.x+1][aktualny.y].h = 10 * (abs(nowa_mapa[aktualny.x+1][aktualny.y].x - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].x) + abs(nowa_mapa[aktualny.x+1][aktualny.y].y - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].y))
                    nowa_mapa[aktualny.x+1][aktualny.y].suma = nowa_mapa[aktualny.x+1][aktualny.y].g + nowa_mapa[aktualny.x+1][aktualny.y].h
                    list_of_item_otwarta.append(nowa_mapa[aktualny.x+1][aktualny.y])
            except:
                pass
            try:
                for Pole in list_of_item_zamknieta:
                    if Pole == nowa_mapa[aktualny.x-1][aktualny.y]:
                        znaleziony = 1
                        break
                    else:
                        znaleziony = 0
                if nowa_mapa[aktualny.x-1][aktualny.y].otwarty and znaleziony == 0 and aktualny.x-1 >= 0:
                    nowa_mapa[aktualny.x-1][aktualny.y].g = 10 * (nowa_mapa[aktualny.x-1][aktualny.y].x + (nowa_mapa[aktualny.x-1][aktualny.y].y - 1))
                    nowa_mapa[aktualny.x-1][aktualny.y].h = 10 * (abs(nowa_mapa[aktualny.x-1][aktualny.y].x - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].x) + abs(nowa_mapa[aktualny.x-1][aktualny.y].y - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].y))
                    nowa_mapa[aktualny.x-1][aktualny.y].suma = nowa_mapa[aktualny.x-1][aktualny.y].g + nowa_mapa[aktualny.x-1][aktualny.y].h
                    list_of_item_otwarta.append(nowa_mapa[aktualny.x-1][aktualny.y])
            except:
                pass
            try:
                for Pole in list_of_item_zamknieta:
                    if Pole == nowa_mapa[aktualny.x][aktualny.y+1]:
                        znaleziony = 1
                        break
                    else:
                        znaleziony = 0
                if nowa_mapa[aktualny.x][aktualny.y+1].otwarty and znaleziony == 0:
                    nowa_mapa[aktualny.x][aktualny.y+1].g = 10 * (nowa_mapa[aktualny.x][aktualny.y+1].x + (nowa_mapa[aktualny.x][aktualny.y+1].y - 1))
                    nowa_mapa[aktualny.x][aktualny.y+1].h = 10 * (abs(nowa_mapa[aktualny.x][aktualny.y+1].x - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].x) + abs(nowa_mapa[aktualny.x][aktualny.y+1].y - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].y))
                    nowa_mapa[aktualny.x][aktualny.y+1].suma = nowa_mapa[aktualny.x][aktualny.y+1].g + nowa_mapa[aktualny.x][aktualny.y+1].h
                    list_of_item_otwarta.append(nowa_mapa[aktualny.x][aktualny.y+1])
            except:
                pass
            try:
                for Pole in list_of_item_zamknieta:
                    if Pole == nowa_mapa[aktualny.x][aktualny.y-1]:
                        znaleziony = 1
                        break
                    else:
                        znaleziony = 0
                if nowa_mapa[aktualny.x][aktualny.y-1].otwarty and znaleziony == 0 and aktualny.y-1 >= 0:
                    nowa_mapa[aktualny.x][aktualny.y-1].g = 10 * (nowa_mapa[aktualny.x][aktualny.y-1].x + (nowa_mapa[aktualny.x][aktualny.y-1].y - 1))
                    nowa_mapa[aktualny.x][aktualny.y-1].h = 10 * (abs(nowa_mapa[aktualny.x][aktualny.y-1].x - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].x) + abs(nowa_mapa[aktualny.x][aktualny.y-1].y - nowa_mapa[len(nowa_mapa)- 1][len(nowa_mapa)- 1].y))
                    nowa_mapa[aktualny.x][aktualny.y-1].suma = nowa_mapa[aktualny.x][aktualny.y-1].g + nowa_mapa[aktualny.x][aktualny.y-1].h
                    list_of_item_otwarta.append(nowa_mapa[aktualny.x][aktualny.y-1])
            except:
                pass
            
            list_of_item_otwarta.remove(aktualny)
            list_of_item_zamknieta.append(aktualny)
            if mapa_ok == 1:
                return True


    def rysuj_mape(self):
        global poziom_p
        global ile_map
        Functions.clear_screen()  # czyszczenie ekranu
        Draw_Images.rysuj("static/LOGO.txt")
        print('\t\t\tDUNGEON LEVEL: ', poziom_p, '\n')

        for i in range(len(self.mapa[0])):
            for j in range(len(self.mapa[0])):
                try:
                    if self.mapa[i][j].otwarty and self.mapa[i][j].widoczny:
                        if i == len(self.mapa[0])-1 and j == len(self.mapa[0])-1:
                            print('X')
                        elif j == len(self.mapa[0]) - 1:
                            print('_')
                        else:
                            if j == 0:
                                print('\t\t\t_', end='')
                            else:
                                print('_', end='')
                    elif not self.mapa[i][j].otwarty and self.mapa[i][j].widoczny:
                        if j == len(self.mapa[0]) - 1:
                            print('#')
                        else:
                            if j == 0:
                                print('\t\t\t#', end='')
                            else:
                                print('#', end='')
                    else:
                        if j == len(self.mapa[0]) - 1:
                            print(' ')
                        else:
                            if j == 0:
                                print('\t\t\t ', end='')
                            else:
                                print(' ', end='')
                except:
                    if j == len(self.mapa[0]) - 1:
                        print('8')
                    else:
                        if j == 0:
                            print('\t\t\t8', end='')
                        else:
                            print('8', end='')

        print('\t\t\t\t\t\tINSTRUCTIONS')
        print('\t\t\t\t\t\t\t8 - PLAYER\tw - go up')
        print('\t\t\t\t\t\t\t_ - OPEN ROOM\ts - go down')
        print('\t\t\t\t\t\t\t# - CLOSED ROOM\ta - go left')
        print('\t\t\t\t\t\t\tX - EXIT\td - go right')
        print('\t\t\t\t\t\t\t\t\tc - show player stats and quests')
        print('\t\t\t\t\t\t\t\t\ti - show inventory')
        print('\n\t\t\t\t\t\t\t\t\t\tg - exit game (game save)')
        print('\tMap nr: ', ile_map)

    def stworz_nowa_mape(self,gr):
        if gr.position[0] == len(self.mapa) - 1 and gr.position[1] == len(self.mapa) - 1:
            global poziom_p
            poziom_p += 1
            self = Mapa()
         
            self.przygotuj_mape()
            self.mapa[0][0] = gr
            gr.take_position(self)
            Functions.widocznosc(gr, self)
            self.rysuj_mape()
        
            Functions.poruszanie_po_mapie(gr, self)
