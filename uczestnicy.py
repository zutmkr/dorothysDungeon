# -*- coding: utf-8 -*-
import random
import winsound
import os
from msvcrt import getch

import przedmiot
import rysuj_obrazy
import podziemia
import pokoj
import funkcje

prawda_falsz = [True, False]
gargulce = 0

class Gracz:

    lista = []  # lista przedmiotow
    pozycja = []
    zadania = []
    punkty = 0
    zloto = 0.0
    imie = ''
    
    def __init__(self):
        self.zadania = [0,0,0,0,0,0]
        self.lista = []
        self.punkty = 0
        self.zloto = 0.0
        
        
    # atrybuty postaci
    s = 15 # sila
    pz = 39  # punkty zycia

    def pokaz_staty(self):
        print('STRENGHT: ', self.s)
        print('LIFE POINTS: ', self.pz)
        print('GOLD: ', self.zloto)
    
    def pokaz_zadania(self):
        if self.zadania[3] == 1 and self.zadania[4] == 1 and self.zadania[5] == 0:
            with open('quests/zadH1.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.zadania[3] == 1 and self.zadania[4] == 1 and self.zadania[5] == 1:
            with open('quests/zadH11.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.zadania[3] == 1 and self.zadania[4] == 0 and gargulce == 0:
            with open('quests/zadH2.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.zadania[3] == 1 and self.zadania[4] == 0 and gargulce == 1:
            with open('quests/zadH21.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.zadania[3] == 1 and self.zadania[4] == 0 and gargulce > 1:
            with open('quests/zadH22.txt', encoding="utf8") as plik:
                print(plik.read())
        else:
            with open('quests/brak.txt', encoding="utf8") as plik:
                print(plik.read())

    def pokaz_plecak(self):
        for Przedmiot in self.lista:
            print(Przedmiot.nazwa)

    def karta_postaci(self):
        os.system('cls')  # czyszczenie ekranu
        print('\n\n\t\t', self.imie, 'GREAT WARRIOR\n\n')
        with open('static/warrior.txt') as plik:
            print(plik.read())
        self.pokaz_staty()
        self.pokaz_zadania()
        
    def pobierz_pozycje(self, maps):
        for i in range(len(maps.mapa)):
            try:
                if maps.mapa[i].index(self) >= 0:
                    self.pozycja = []
                    self.pozycja.append(i)
                    self.pozycja.append(maps.mapa[i].index(self))
            except:
                continue

    def dodaj_do_plecak(self):
        if random.choice(prawda_falsz):
            self.lista.append(przedmiot.Wartosciowy().dodaj_przedmiot())
            self.punkty += 1
            funkcje.status = ''
            if not self.lista[-1].nazwa.find('legendary'):
                self.lista[-1].nazwa += ' +5 do STRENGHT'
                winsound.PlaySound('sound/legenda.wav', winsound.SND_ASYNC)
                funkcje.status = 'You got ' + self.lista[-1].nazwa + '!!!'          
                self.s += 5
        else:
            self.lista.append(przedmiot.Smiec().dodaj_przedmiot())
            self.punkty -= 1
            funkcje.status = ''
            

    def sprzedaj_kup(self, kto, wyb, s):
        inp = ''
        if not self.lista:
            print('(',self.imie,'): I do not have any goods with me...')
            getch()
            
        while inp != '8':
            if not self.lista:
                break
    
            for Przedmiot in self.lista:
                Przedmiot.nazwa = '   ' + Przedmiot.nazwa
    
            self.lista[s].nazwa = self.lista[s].nazwa.lstrip()
            self.lista[s].nazwa = '-> ' + self.lista[s].nazwa
    
            os.system('cls')  # czyszczenie ekranu
            print('Choose what interests you:')
            print('\t\t\t\t\t\tINSTRUCTIONS')
            print('\t\t\t\t\t\t\tw - arrow up')
            print('\t\t\t\t\t\t\ts - arrow down')
            if type(self) is Handlarz: 
                print('\t\t   BUY\t\t\t\tk - buy item')
            else:
                print('\t\tSELL\t\t\t\tk - sell item')
            print('\t\t\t\t\t\t\t8 - go back to the conversation with the trader')
            if type(self) is Handlarz:
                print('\t\tYour gold:', kto.zloto, '\n')
            else:
                print('\t\tYour gold:', self.zloto, '\n')
            for Przedmiot in self.lista:
                dlugosc_str = 34 - len(Przedmiot.nazwa)
                print('\t', Przedmiot.nazwa, ' ' * dlugosc_str, Przedmiot.wartosc, ' gold')
    
            inp = getch().decode("utf-8")
            if inp == 'w':
                s -= 1
                try:
                    if s < 0:
                        s = 0
                        self.lista[s + 1].nazwa = self.lista[s + 1].nazwa.lstrip()
                        self.lista[s + 1].nazwa = self.lista[s + 1].nazwa.lstrip('-> ')
                        self.lista[s + 1].nazwa = '   ' + self.lista[s + 1].nazwa
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip()
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip('-> ')
                        self.lista[s].nazwa = '-> ' + self.lista[s].nazwa
                    else:
                        self.lista[s + 1].nazwa = self.lista[s + 1].nazwa.lstrip()
                        self.lista[s + 1].nazwa = self.lista[s + 1].nazwa.lstrip('-> ')
                        self.lista[s + 1].nazwa = '   ' + self.lista[s + 1].nazwa
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip()
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip('-> ')
                        self.lista[s].nazwa = '-> ' + self.lista[s].nazwa
                except:
                    pass
            elif inp == 's':
                s += 1
                try:
                    if s > len(self.lista) - 1:
                        s = len(self.lista) - 1
                        self.lista[s - 1].nazwa = self.lista[s - 1].nazwa.lstrip()
                        self.lista[s - 1].nazwa = self.lista[s - 1].nazwa.lstrip('-> ')
                        self.lista[s - 1].nazwa = '   ' + self.lista[s - 1].nazwa
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip()
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip('-> ')
                        self.lista[s].nazwa = '-> ' + self.lista[s].nazwa
                    else:
                        self.lista[s - 1].nazwa = self.lista[s - 1].nazwa.lstrip()
                        self.lista[s - 1].nazwa = self.lista[s - 1].nazwa.lstrip('-> ')
                        self.lista[s - 1].nazwa = '   ' + self.lista[s - 1].nazwa
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip()
                        self.lista[s].nazwa = self.lista[s].nazwa.lstrip('-> ')
                        self.lista[s].nazwa = '-> ' + self.lista[s].nazwa
                except:
                    pass
            elif inp == 'k':
                if type(self) is Handlarz:
                    for Przedmiot in self.lista:
                        if not Przedmiot.nazwa.find('-> '):
                            if kto.zloto < Przedmiot.wartosc:
                                print("I can not afford it, I have too little GOLD!")
                                getch()
                                break
                            Przedmiot.nazwa = Przedmiot.nazwa.lstrip('-> ')
                            self.zloto += Przedmiot.wartosc
                            kto.zloto -= Przedmiot.wartosc
                            kto.lista.append(Przedmiot)
                            if not Przedmiot.nazwa.find('legendary'):
                                kto.s += 5
                            self.lista.remove(Przedmiot)
                            s = 0
                else:
                    for Przedmiot in self.lista:
                        if not Przedmiot.nazwa.find('-> '):
                            if kto.zloto < Przedmiot.wartosc:
                                print("The merchant does not have so much GOLD to buy it!")
                                getch()
                                break
                            Przedmiot.nazwa = Przedmiot.nazwa.lstrip('-> ')
                            self.zloto += Przedmiot.wartosc
                            kto.zloto -= Przedmiot.wartosc
                            kto.lista.append(Przedmiot)
                            if not Przedmiot.nazwa.find('legendary'):
                                self.s -= 5
                            self.lista.remove(Przedmiot)
                            s = 0
                            
            for Przedmiot in self.lista:
                Przedmiot.nazwa = Przedmiot.nazwa.lstrip()
                Przedmiot.nazwa = Przedmiot.nazwa.lstrip('-> ')
        
    def quest(self,gr):        
        while True:
            os.system('cls')  # czyszczenie ekranu
            rysuj_obrazy.rysuj("static/" + self.imie + ".txt")  
            od = 1
            do = 3
            rysuj_obrazy.rysuj_oddo("quests/" + self.imie + ".txt",od,do)
            print('\tt - YES\tn - NO')
            inp = input()
            #inp = getch().decode("utf-8")
            if inp == 't':    
                if type(self) is Uzdrowiciel:
                    gr.zadania[0] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        rysuj_obrazy.rysuj_oddo("quests/" + self.imie + ".txt",5,7)
                        gr.zadania[1] = 1
                        getch()
                        print('(' + gr.imie + '): It will be done!')
                        getch()
                    else:   #DRUGIE ZADANIE
                        rysuj_obrazy.rysuj_oddo("quests/" + self.imie + ".txt",17,19)
                        gr.zadania[1] = 0
                        getch()
                        print('(' + gr.imie + '): It will be done!')
                        getch()           
                else:   #HANDLARZ
                    gr.zadania[3] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        rysuj_obrazy.rysuj_oddo("quests/" + self.imie + ".txt",5,8)
                        gr.zadania[4] = 1
                        getch()
                        print('(' + gr.imie + '): It will be done!')
                        getch()
                    else:   #DRUGIE ZADANIE
                        rysuj_obrazy.rysuj_oddo("quests/" + self.imie + ".txt",22,24)
                        gr.zadania[4] = 0
                        getch()
                        print('(' + gr.imie + '): It will be done!')
                        getch()
                return False
            elif inp == 'n':
                print('Bye then...')
                getch()
                return False
            
class Potwor(Gracz):
    def __init__(self,imie,s,pz):
        self.imie = imie
        self.s = s
        self.pz = pz
        self.pmax = pz

    def walka_gui(self, status, gr):
        os.system('cls')
        rysuj_obrazy.rysuj('static/' + self.imie + '.txt')
        print('You must fight with ', self.imie, ' ', self.pz, '/', self.pmax, 'LP')
        print('\t\t\t\t\t\tCOMMANDS')
        print('\t\t\t\t\t\t\tf - Weapon attack')
        print('\t\t\t\t\t\t\tj - Run(25% chance)\n\n')
        print('\t\t\t\t\t\t\tYour LP: ', gr.pz)
        print('Status: ', status)


class Uzdrowiciel(Gracz):
    def __init__(self, gr):
        self.imie = 'uzdr'
        os.system('cls')  # czyszczenie ekranu
        rysuj_obrazy.rysuj('static/uzdr.txt')
        ile_pkt = 3 * 1.5 * podziemia.poziom_p
        print('You meet the Healer!!!')
        print('You receive', int(ile_pkt), 'additional LIFE POINTS')
        #funkcje.quest()
        
        gr.pz += int(ile_pkt)
        getch()
    
class Handlarz(Gracz):
    def __init__(self):
        self.zloto = 500.0
    lista = []
    imie = 'handl'







