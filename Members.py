# -*- coding: utf-8 -*-
import random
import os
import Item
import Draw_Images
import Undergrounds
import Room
import Functions

true_or_false = [True, False]
gargulce = 0

class Player:

    list_of_item = []  # list_of_item Itemow
    position = []
    tasks = []
    points = 0
    gold = 0.0
    name = ''
    
    def __init__(self):
        self.tasks = [0,0,0,0,0,0]
        self.list_of_item = []
        self.points = 0
        self.gold = 0.0
        
        
    # atrybuty postaci
    s = 15 # sila
    pz = 39  # points zycia

    def show_stats(self):
        print('STRENGHT: ', self.s)
        print('LIFE POINTS: ', self.pz)
        print('GOLD: ', self.gold)
    
    def show_tasks(self):
        if self.tasks[3] == 1 and self.tasks[4] == 1 and self.tasks[5] == 0:
            with open('quests/zadH1.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 1 and self.tasks[5] == 1:
            with open('quests/zadH11.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce == 0:
            with open('quests/zadH2.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce == 1:
            with open('quests/zadH21.txt', encoding="utf8") as plik:
                print(plik.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce > 1:
            with open('quests/zadH22.txt', encoding="utf8") as plik:
                print(plik.read())
        else:
            with open('quests/brak.txt', encoding="utf8") as plik:
                print(plik.read())

    def show_backpack(self):
        for Item in self.list_of_item:
            print(Item.name)

    def character_card(self):
        Functions.clear_screen()  # czyszczenie ekranu
        print('\n\n\t\t', self.name, 'GREAT WARRIOR\n\n')
        with open('static/warrior.txt') as plik:
            print(plik.read())
        self.show_stats()
        self.show_tasks()
        
        
    def take_position(self, maps):
        for i in range(len(maps.mapa)):
            try:
                if maps.mapa[i].index(self) >= 0:
                    self.position = []
                    self.position.append(i)
                    self.position.append(maps.mapa[i].index(self))
            except:
                continue

    def add_to_backpack(self):
        if random.choice(true_or_false):
            self.list_of_item.append(Item.Value_item().Add_Item())
            self.points += 1
            Functions.status = ''
            if not self.list_of_item[-1].name.find('legendary'):
                self.list_of_item[-1].name += ' +5 do STRENGHT'
                #winsound.PlaySound('sound/legenda.wav', winsound.SND_ASYNC)
                Functions.status = 'You got ' + self.list_of_item[-1].name + '!!!'          
                self.s += 5
        else:
            self.list_of_item.append(Item.trash_item().Add_Item())
            self.points -= 1
            Functions.status = ''
            

    def sprzedaj_kup(self, kto, wyb, s):
        inp = ''
        if not self.list_of_item:
            print('(',self.name,'): I do not have any goods with me...')
            Functions.get_char()
            
        while inp != '8':
            if not self.list_of_item:
                break
    
            for Item in self.list_of_item:
                Item.name = '   ' + Item.name
    
            self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
            self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
    
            Functions.clear_screen()  # czyszczenie ekranu
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
                print('\t\tYour gold:', kto.gold, '\n')
            else:
                print('\t\tYour gold:', self.gold, '\n')
            for Item in self.list_of_item:
                dlugosc_str = 34 - len(Item.name)
                print('\t', Item.name, ' ' * dlugosc_str, Item.value, ' gold')
    
            inp = input()
            if inp == 'w':
                s -= 1
                try:
                    if s < 0:
                        s = 0
                        self.list_of_item[s + 1].name = self.list_of_item[s + 1].name.lstrip()
                        self.list_of_item[s + 1].name = self.list_of_item[s + 1].name.lstrip('-> ')
                        self.list_of_item[s + 1].name = '   ' + self.list_of_item[s + 1].name
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip('-> ')
                        self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
                    else:
                        self.list_of_item[s + 1].name = self.list_of_item[s + 1].name.lstrip()
                        self.list_of_item[s + 1].name = self.list_of_item[s + 1].name.lstrip('-> ')
                        self.list_of_item[s + 1].name = '   ' + self.list_of_item[s + 1].name
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip('-> ')
                        self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
                except:
                    pass
            elif inp == 's':
                s += 1
                try:
                    if s > len(self.list_of_item) - 1:
                        s = len(self.list_of_item) - 1
                        self.list_of_item[s - 1].name = self.list_of_item[s - 1].name.lstrip()
                        self.list_of_item[s - 1].name = self.list_of_item[s - 1].name.lstrip('-> ')
                        self.list_of_item[s - 1].name = '   ' + self.list_of_item[s - 1].name
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip('-> ')
                        self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
                    else:
                        self.list_of_item[s - 1].name = self.list_of_item[s - 1].name.lstrip()
                        self.list_of_item[s - 1].name = self.list_of_item[s - 1].name.lstrip('-> ')
                        self.list_of_item[s - 1].name = '   ' + self.list_of_item[s - 1].name
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
                        self.list_of_item[s].name = self.list_of_item[s].name.lstrip('-> ')
                        self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
                except:
                    pass
            elif inp == 'k':
                if type(self) is Handlarz:
                    for Item in self.list_of_item:
                        if not Item.name.find('-> '):
                            if kto.gold < Item.value:
                                print("I can not afford it, I have too little GOLD!")
                                Functions.get_char()
                                break
                            Item.name = Item.name.lstrip('-> ')
                            self.gold += Item.value
                            kto.gold -= Item.value
                            kto.list_of_item.append(Item)
                            if not Item.name.find('legendary'):
                                kto.s += 5
                            self.list_of_item.remove(Item)
                            s = 0
                else:
                    for Item in self.list_of_item:
                        if not Item.name.find('-> '):
                            if kto.gold < Item.value:
                                print("The merchant does not have so much GOLD to buy it!")
                                Functions.get_char()
                                break
                            Item.name = Item.name.lstrip('-> ')
                            self.gold += Item.value
                            kto.gold -= Item.value
                            kto.list_of_item.append(Item)
                            if not Item.name.find('legendary'):
                                self.s -= 5
                            self.list_of_item.remove(Item)
                            s = 0
                            
            for Item in self.list_of_item:
                Item.name = Item.name.lstrip()
                Item.name = Item.name.lstrip('-> ')
        
    def quest(self,gr):        
        while True:
            Functions.clear_screen()  # czyszczenie ekranu
            Draw_Images.rysuj("static/" + self.name + ".txt")  
            od = 1
            do = 3
            Draw_Images.rysuj_oddo("quests/" + self.name + ".txt",od,do)
            print('\tt - YES\tn - NO')
            inp = input()
            if inp == 't':    
                if type(self) is Uzdrowiciel:
                    gr.tasks[0] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        Draw_Images.rysuj_oddo("quests/" + self.name + ".txt",5,7)
                        gr.tasks[1] = 1
                        Functions.get_char()
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                    else:   #DRUGIE ZADANIE
                        Draw_Images.rysuj_oddo("quests/" + self.name + ".txt",17,19)
                        gr.tasks[1] = 0
                        Functions.get_char()
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()           
                else:   #HANDLARZ
                    gr.tasks[3] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        Draw_Images.rysuj_oddo("quests/" + self.name + ".txt",5,8)
                        gr.tasks[4] = 1
                        Functions.get_char()
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                    else:   #DRUGIE ZADANIE
                        Draw_Images.rysuj_oddo("quests/" + self.name + ".txt",22,24)
                        gr.tasks[4] = 0
                        Functions.get_char()
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                return False
            elif inp == 'n':
                print('Bye then...')
                Functions.get_char()
                return False
            
class Potwor(Player):
    def __init__(self,name,s,pz):
        self.name = name
        self.s = s
        self.pz = pz
        self.pmax = pz

    def walka_gui(self, status, gr):
        Functions.clear_screen()
        Draw_Images.rysuj('static/' + self.name + '.txt')
        print('You must fight with ', self.name, ' ', self.pz, '/', self.pmax, 'LP')
        print('\t\t\t\t\t\tCOMMANDS')
        print('\t\t\t\t\t\t\tf - Weapon attack')
        print('\t\t\t\t\t\t\tj - Run(25% chance)\n\n')
        print('\t\t\t\t\t\t\tYour HP: ', gr.pz)
        print('Status: ', status)


class Uzdrowiciel(Player):
    def __init__(self, gr):
        self.name = 'uzdr'
        Functions.clear_screen()  # czyszczenie ekranu
        Draw_Images.rysuj('static/uzdr.txt')
        ile_pkt = 3 * 1.5 * Undergrounds.poziom_p
        print('You meet the Healer!!!')
        print('You receive', int(ile_pkt), 'additional LIFE POINTS')
        #Functions.quest()
        
        gr.pz += int(ile_pkt)
        Functions.get_char()
    
class Handlarz(Player):
    def __init__(self):
        self.gold = 500.0
    list_of_item = []
    name = 'handl'







