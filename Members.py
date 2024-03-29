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
    strength = 15 # sila
    life_points = 39  # points zycia

    def show_stats(self):
        print('STRENGHT: ', self.strength)
        print('LIFE POINTS: ', self.life_points)
        print('GOLD: ', self.gold)
    
    def show_tasks(self):
        if self.tasks[3] == 1 and self.tasks[4] == 1 and self.tasks[5] == 0:
            with open('quests/zadH1.txt', encoding="utf8") as file:
                print(file.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 1 and self.tasks[5] == 1:
            with open('quests/zadH11.txt', encoding="utf8") as file:
                print(file.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce == 0:
            with open('quests/zadH2.txt', encoding="utf8") as file:
                print(file.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce == 1:
            with open('quests/zadH21.txt', encoding="utf8") as file:
                print(file.read())
        elif self.tasks[3] == 1 and self.tasks[4] == 0 and gargulce > 1:
            with open('quests/zadH22.txt', encoding="utf8") as file:
                print(file.read())
        else:
            with open('quests/brak.txt', encoding="utf8") as file:
                print(file.read())

    def show_backpack(self):
        for item in self.list_of_item:
            print(item.name)

    def character_card(self):
        Functions.clear_screen()  # czyszczenie ekranu
        print('\n\n\t\t', self.name, 'GREAT WARRIOR\n\n')
        with open('static/warrior.txt') as file:
            print(file.read())
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
                self.list_of_item[-1].name += ' +5 to STRENGHT'
                #winsound.PlaySound('sound/legenda.wav', winsound.SND_ASYNC)
                Functions.status = 'You got ' + self.list_of_item[-1].name + '!!!'          
                self.strength += 5
        else:
            self.list_of_item.append(Item.trash_item().Add_Item())
            self.points -= 1
            Functions.status = ''
            

    def sprzedaj_kup(self, kto, wyb, s):
        keyboard_key = ''
        if not self.list_of_item:
            print('(',self.name,'): I do not have any goods with me...')
            Functions.getch()

        while keyboard_key != 'esc':
            if not self.list_of_item:
                break
    
            for item in self.list_of_item:
                item.name = '   ' + item.name
    
            self.list_of_item[s].name = self.list_of_item[s].name.lstrip()
            self.list_of_item[s].name = '-> ' + self.list_of_item[s].name
    
            Functions.clear_screen()  # czyszczenie ekranu
            print('Choose what interests you:')
            print('\t\t\t\t\t\tINSTRUCTIONS')
            print('\t\t\t\t\t\tw - arrow up')
            print('\t\t\t\t\t\ts - arrow down')
            if type(self) is Merchant: 
                print('\t\t   BUY\t\t\t\tEnter - buy item')
            else:
                print('\t\tSELL\t\t\t\tEnter - sell item')
            print('\t\t\t\t\t\tEsc - go back to the conversation with the trader')
            if type(self) is Merchant:
                print('\t\tYour gold:', kto.gold, '\n')
            else:
                print('\t\tYour gold:', self.gold, '\n')
            for item in self.list_of_item:
                dlugosc_str = 34 - len(item.name)
                print('\t', item.name, ' ' * dlugosc_str, item.value, ' gold')
            keyboard_key = Functions.getkey()
            if keyboard_key == 'w':
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
            elif keyboard_key == 's':
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
            elif keyboard_key == 'return':
                if type(self) is Merchant:
                    for item in self.list_of_item:
                        if not item.name.find('-> '):
                            if kto.gold < item.value:
                                print("I can not afford it, I have too little GOLD!")
                                Functions.get_char()
                                break
                            item.name = item.name.lstrip('-> ')
                            self.gold += item.value
                            kto.gold -= item.value
                            kto.list_of_item.append(item)
                            if not item.name.find('legendary'):
                                kto.strength += 5
                            self.list_of_item.remove(item)
                            s = 0
                else:
                    for item in self.list_of_item:
                        if not item.name.find('-> '):
                            if kto.gold < item.value:
                                print("The merchant does not have so much GOLD to buy it!")
                                Functions.get_char()
                                break
                            item.name = item.name.lstrip('-> ')
                            self.gold += item.value
                            kto.gold -= item.value
                            kto.list_of_item.append(item)
                            if not item.name.find('legendary'):
                                self.strength -= 5
                            self.list_of_item.remove(item)
                            s = 0
                            
            for item in self.list_of_item:
                item.name = item.name.lstrip()
                item.name = item.name.lstrip('-> ')
        
    def quest(self,gr):        
        while True:
            Functions.clear_screen()  # czyszczenie ekranu
            if type(self) is Uzdrowiciel:
                Draw_Images.draw("static/uzdr.txt")  
                od = 1
                do = 3
                Draw_Images.rysuj_oddo("quests/uzdr.txt",od,do)
            else:
                Draw_Images.draw("static/handl.txt")  
                od = 1
                do = 3
                Draw_Images.rysuj_oddo("quests/handl.txt",od,do)
            print('\tt - YES\tn - NO')
            inp = input()
            if inp == 't':    
                if type(self) is Uzdrowiciel:
                    gr.tasks[0] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        Draw_Images.rysuj_oddo("quests/uzdr.txt",5,7)
                        gr.tasks[1] = 1
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                    else:   #DRUGIE ZADANIE
                        Draw_Images.rysuj_oddo("quests/uzdr.txt",17,19)
                        gr.tasks[1] = 0
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()           
                else:   #HANDLARZ
                    gr.tasks[3] = 1
                    r = random.choice([True, False])
                    if r:   #PIERWSZE ZADANIE
                        Draw_Images.rysuj_oddo("quests/handl.txt",5,8)
                        gr.tasks[4] = 1
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                    else:   #DRUGIE ZADANIE
                        Draw_Images.rysuj_oddo("quests/handl.txt",22,24)
                        gr.tasks[4] = 0
                        print('(' + gr.name + '): It will be done!')
                        Functions.get_char()
                return False
            elif inp == 'n':
                print('Bye then...')
                Functions.get_char()
                return False
            
class Potwor(Player):
    def __init__(self,name, s, life_points):
        self.name = name
        self.strength = s
        self.life_points = life_points
        self.pmax = life_points

    def walka_gui(self, status, gr):
        Functions.clear_screen()
        Draw_Images.draw('static/' + self.name + '.txt')
        print('You must fight with ', self.name, ' ', self.life_points, '/', self.pmax, 'LP')
        print('\t\t\t\t\t\tCOMMANDS')
        print('\t\t\t\t\t\t\tf - Weapon attack')
        print('\t\t\t\t\t\t\tj - Run(25% chance)\n\n')
        print('\t\t\t\t\t\t\tYour HP: ', gr.life_points)
        print('Status: ', status)


class Uzdrowiciel(Player):
    def __init__(self, gr):
        self.name = 'uzdr'
        Functions.clear_screen()  # czyszczenie ekranu
        Draw_Images.draw('static/uzdr.txt')
        ile_pkt = 3 * 1.5 * Undergrounds.poziom_p
        print('You meet the Healer!!!')
        print('You receive', int(ile_pkt), 'additional LIFE POINTS')
        #Functions.quest()
        
        gr.life_points += int(ile_pkt)
        Functions.get_char()
    
class Merchant(Player):
    def __init__(self):
        self.gold = 500.0
    list_of_item = []
    name = 'Merchant'







