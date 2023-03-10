# -*- coding: utf-8 -*-
import random
import os, sys, termios, tty
import pickle
import logging
from time import sleep

import Room
import Members
import Undergrounds
import Draw_Images


logging.basicConfig(filename='error_logs/errors.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)


prawda_falsz = [True, False]
status = ''
PIK = "save/objects.bj"

def get_char(skip_text=True):
    if skip_text:
      input(f'Press Enter key to continue...')
    else:
      input()

def clear_screen():
	os.system('clear')
	
def sciana():
    global status
    status = 'It is a wall.'
    
def zapisz_gre(gr,maps):
    data = [gr,maps, Undergrounds.poziom_p, gr.list_of_item, gr.tasks]
    
    with open(PIK, "w+b") as f:
        pickle.dump(len(data), f)
        for value in data:
            pickle.dump(value, f)
            
def handel(gr,ha):
    wyb = ''

    ha.add_to_backpack()
    ha.add_to_backpack()
    ha.add_to_backpack()

    
    while wyb != '0':
        clear_screen()  # czyszczenie ekranu
        Draw_Images.rysuj('static/handl.txt')
        print('\t\tYou meet a merchant!!!\n')
        print('>How can I help you?\n\t\t\t The dealer has ', ha.gold, ' gold\n')
        print('\t1) Show me your goods. (Buy)')
        print('\t2) See what I have. (Sell)')
        if gr.tasks[3] == 1 and gr.tasks[5] == 1:
            print('\t3) Give the quest back (Get the prize!)')
        print('\t0) Goodbye.\t\t Your gold: ', gr.gold)
        print('CURRENT STRENGTH:', gr.strength)
        wyb = input('\nYour choice: ')
        s = 0
        if wyb == '1':
            ha.sprzedaj_kup(gr,wyb,s)
        elif wyb == '2':
            gr.sprzedaj_kup(ha,wyb,s)
        elif gr.tasks[3] == 1 and gr.tasks[4] == 1 and gr.tasks[5] == 1:
            print ("You are POWERFUL! \n\
            Thanks for destroying the last \n\
            representative of his species. Here's the promised \n\
            prize.")
            ###
            # I need to add some kind of sleep or button press for 
            # akcnowledge
            gr.add_to_backpack()
            gr.points += 10
            gr.tasks[3] = 0
            gr.tasks[4] = 0
            gr.tasks[5] = 0
            print("You received an item! - ", gr.list_of_item[-1].name)
            ###
            # I need to add some kind of sleep or button press for 
            # akcnowledge
        elif gr.tasks[3] == 1 and gr.tasks[4] == 0 and gr.tasks[5] == 1:
            print ("\tYou are GREAT! \n\
            These gargoyles will not come back soon. \n\
            In the end, I will have peace. Here's the promised \n\
            prize.")
            ###
            # I need to add some kind of sleep or button press for 
            # akcnowledge
            gr.add_to_backpack()
            gr.points += 20
            gr.tasks[3] = 0
            gr.tasks[4] = 0
            gr.tasks[5] = 0
            Members.gargulce = 0
            print("You received an item! - ", gr.list_of_item[-1].name)
            ###
            # I need to add some kind of sleep or button press for 
            # akcnowledge
    try:
        if random.choice(prawda_falsz):
            if gr.tasks[3] == 0:
                ha.quest(gr)
    except Exception as e:
        logger.error(e)    
      
def event(gr, maps):
    ha = Members.Merchant()
    ha.gold *= Undergrounds.poziom_p * 1.25
    p = random.randint(0,3)
    #p = 1
    if p == 0:
        Members.Uzdrowiciel(gr)
    elif p == 1:
        handel(gr,ha)
    else:
        rozpocznij_walke(gr)

def widocznosc(gr, maps):
    # boki dolne
    if gr.position[0] < len(maps.mapa) and gr.position[1] < len(maps.mapa):
        try:
            maps.mapa[gr.position[0] + 1][gr.position[1]].widoczny = True
        except:
            pass
        try:
            maps.mapa[gr.position[0] + 1][gr.position[1] + 1].widoczny = True  # dp
        except:
            pass

    # boki gorne
    if gr.position[0] > 0 and gr.position[1] < len(maps.mapa):
        try:
            maps.mapa[gr.position[0] - 1][gr.position[1]].widoczny = True
        except:
            pass
        try:
            maps.mapa[gr.position[0] - 1][gr.position[1] + 1].widoczny = True  # gp
        except:
            pass
        try:
            maps.mapa[gr.position[0]][gr.position[1] + 1].widoczny = True
        except:
            pass

    # bok lewy
    if gr.position[1] > 0 and gr.position[0] > 0:
        try:
            maps.mapa[gr.position[0]][gr.position[1] - 1].widoczny = True
        except:
            pass
        try:
            maps.mapa[gr.position[0] + 1][gr.position[1] - 1].widoczny = True  # dl
        except:
            pass
        try:
            maps.mapa[gr.position[0] - 1][gr.position[1] - 1].widoczny = True  # gl
        except:
            pass

    try:
        maps.mapa[gr.position[0]][gr.position[1] + 1].widoczny = True
    except:
        pass


def poruszanie_po_mapie(gr, maps):
    global status
    gr.take_position(maps)

    while True:
        print('Status: ', status)
        if gr.life_points == 0:
            sys.exit(0)
        h = input('\n\nQuo vadis?>')

        if h == 'w':
            w(gr, maps)
        elif h == 's':
            s(gr, maps)
            maps.stworz_nowa_mape(gr)
        elif h == 'a':
            a(gr, maps)
        elif h == 'd':
            d(gr, maps)
            maps.stworz_nowa_mape(gr)
        elif h == 'c':
            gr.character_card()
            get_char()
        elif h == 'i':
            gr.show_backpack()
            get_char()
        elif h == 'g':
            zapisz_gre(gr,maps)
            print('See you hero!')
            sleep(2)
            sys.exit(0)
        else:
            status = 'You walk along the wrong path!'
        widocznosc(gr, maps)
        maps.rysuj_mape()        
        
        
def stala_position(gr, maps):
    global status
    maps.mapa[gr.position[0]][gr.position[1]] = Room.Pokoj()
    maps.mapa[gr.position[0]][gr.position[1]].Item = False
    gr.take_position(maps)


def w(gr, maps):
    if gr.position[0] - 1 >= 0 and maps.mapa[gr.position[0] - 1][gr.position[1]].otwarty:
        try:
            if maps.mapa[gr.position[0] - 1][gr.position[1]].event:
                event(gr, maps)
        except:
            pass
        maps.mapa[gr.position[0] - 1][gr.position[1]] = gr
        stala_position(gr, maps)
    else:
        sciana()


def s(gr, maps):
    if gr.position[0] + 1 < len(maps.mapa) and maps.mapa[gr.position[0] + 1][gr.position[1]].otwarty:
        try:
            if maps.mapa[gr.position[0] + 1][gr.position[1]].event:
                event(gr, maps)
        except Exception as e:  
          print('ERROR Cannot launch event: '+ str(e))
          get_char()
        maps.mapa[gr.position[0] + 1][gr.position[1]] = gr
        stala_position(gr, maps)
    else:
        sciana()


def a(gr, maps):
    if gr.position[1] - 1 >= 0 and maps.mapa[gr.position[0]][gr.position[1] - 1].otwarty:
        try:
            if maps.mapa[gr.position[0]][gr.position[1] - 1].event:
                event(gr, maps)
        except:
            pass
        maps.mapa[gr.position[0]][gr.position[1] - 1] = gr
        stala_position(gr, maps)
    else:
        sciana()


def d(gr, maps):
    if gr.position[1] + 1 < len(maps.mapa) and maps.mapa[gr.position[0]][gr.position[1] + 1].otwarty:
        try:
            if maps.mapa[gr.position[0] + 1][gr.position[1] + 1].event:
                event(gr, maps)
        except:
            pass
        maps.mapa[gr.position[0]][gr.position[1] + 1] = gr
        stala_position(gr, maps)
    else:
        sciana()        
        
        
def rozpocznij_walke(gr):
    global status

    losuj_potwora = random.randint(1,5)
    if losuj_potwora == 1:
        potwor = Members.Potwor('Smok', 13, 30)
    elif losuj_potwora == 2:
        potwor = Members.Potwor('Niedzwiedz', 13, 30)
    elif losuj_potwora == 3:
        potwor = Members.Potwor('Gargulec', 13, 30)
    elif gr.tasks[3] == 1 and gr.tasks[4] == 1 and gr.tasks[5] == 0:
        potwor = Members.Potwor('Jezdziec', 6, 45)
    else:
        potwor = Members.Potwor('Demon', 13, 30)

    if Undergrounds.poziom_p > 1:
        potwor.life_points = int(potwor.life_points * Undergrounds.poziom_p * 0.8)
        potwor.pmax = int(potwor.pmax * Undergrounds.poziom_p  * 0.8)
        potwor.strength = int(potwor.strength * Undergrounds.poziom_p * 0.6)

    status = ''    
    

    while True:
        if gr.life_points == 0:
            potwor.walka_gui(status, gr)
            print('YOU WERE SLAIN.')
            get_char()
            
            dlugosc_poziom = ((9 + len(gr.name)) - 19) * (-1)       #magic numbers...
            dlugosc_points = 33 - 9 - len(gr.name) - dlugosc_poziom
            
            
            with open("score/high_score.txt", "a") as f:
                f.write("\n         " + gr.name + (" " * dlugosc_poziom) + str(Undergrounds.poziom_p) + (" " * dlugosc_points) + str(gr.points))
            Draw_Images.rysuj_animacja_ciag('animated/gameover/gameover.txt', 0.035)
            f.close()
            
            Draw_Images.rysuj("score/high_score.txt")
            print('\n\n\t\tBegin a new game?')
            print('\t\t1. New game\t2.Main menu \t3. End game')
            while True:
                d = input('\t\tYour choice?>')
                if d == '1':
                    from __main__ import nowa_gra
                    nowa_gra()
                elif d == '2':
                    from __main__ import menu_glowne
                    menu_glowne()
                elif d == '3':
                    sys.exit(0)
   
        potwor.walka_gui(status, gr)
        h = input('\n\nCommand?>')

        while True:
            if h == 'f':
                status = 'You attack ' + str(potwor.name) + ' for ' + str(gr.strength) + ' damage!'
                potwor.walka_gui(status, gr)
                get_char()
                potwor.life_points -= gr.strength
                break
            elif h == 'j':
                b = random.randrange(1, 13)
                if b in range(1, 5):
                    print('ESCAPE SUCCESSFUL!')
                    get_char()
                    return
                else:
                    print('YOU FAILED TO ESCAPE')
                    get_char()
                    break
            else:
                status = 'I think you got something wrong?!'
                potwor.walka_gui(status, gr)
                h = input('\n\nCommand?>')

        if potwor.life_points <= 0:
            print('VICTORY!!!')
            if potwor.name == "Jezdziec":
                ile_wygral = 135.0 * 1.45 * Undergrounds.poziom_p
                gr.tasks[5] = 1
            elif potwor.name == "Gargulec" and gr.tasks[3] == 1 and gr.tasks[4] == 0:
                ile_wygral = 135.0 * 1.45 * Undergrounds.poziom_p
                if Members.gargulce > 1:
                    gr.tasks[5] = 1
                else:
                    Members.gargulce = Members.gargulce + 1
            else:
                ile_wygral = 100.0 * 1.25 * Undergrounds.poziom_p
                
            gr.gold += ile_wygral
            if random.choice(prawda_falsz):
                gr.add_to_backpack()
                print("You receive {0} gold and {1}.".format(ile_wygral, gr.list_of_item[-1].name))
            else:
                print("You receive ", ile_wygral, " gold.")
            gr.points += 5
            get_char()
            return
        else:
            status = str(potwor.name) + ' attack you for ' + str(potwor.strength) + ' damage!'
            gr.life_points -= potwor.strength
            if gr.life_points <= 0:
                gr.life_points = 0        

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left',
                97: 'a',
                100: 'd',
                115: 's',
                119: 'w'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
