# -*- coding: utf-8 -*-
import os, os.path
import random
import uczestnicy
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from podziemia import Mapa
from tkinter import filedialog

NR_OF_LVL_GEN = 1
mapsgen = 0
WINDOW_TITLE = "Dorothy\'s Dungeon Map Generator v0.05"
WINDOW_RESOLUTION = "630x500"

def licz_pliki(adres):
    ile = 0
    for f in os.listdir(adres):
        if os.path.isfile(os.path.join(adres, f)):
            ile += 1
    return ile


def wyjdz(okno):
    global mapsgen
    mapsgen = 0
    okno.destroy()


def wczytaj_mape(mapa_odkryta):
    d = filedialog.askopenfilename(initialdir = "./mapy") 
    f = open(d, 'r', encoding="utf8")
    mapa_odkryta.delete(1.0, END)
    mapa_odkryta.insert(END, f.read())
    f.close()


def zapisz_mape(mapa_odkryta):
    adres = './mapy'
    a = (str(datetime.now())).split()
    f = open('mapy/' + a[0]+ '_' + str(licz_pliki(adres)) + '.map', 'w', encoding="utf8")
    f.write(mapa_odkryta.get("1.0", "end-1c"))
    f.close()


def zagraj(poziom_pgen, wielkosc_mapygen, punkty_zycia, sila, okno):
    global mapsgen
    if mapsgen == 0:
        messagebox.showinfo("ERROR", "Generate map first to play it!")
    else:    
        okno.destroy()
        from main import nowa_gra
        nowa_gra(poziom_pgen, wielkosc_mapygen, punkty_zycia, sila)

        
def generator():
    def losuj():
        if random_enabled.get() == 1:    
            s.config(state="disabled")

            s1.config(state="disabled")

            hp.config(state="disabled")
            
            ps.config(state="disabled")
        else:
            s['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9)
            s.config(state="readonly")

            s1['values'] = (7, 8, 9, 10, 11, 12, 13, 14)
            s1.config(state="readonly")

            hp['values'] = (39, 60, 100)
            hp.config(state="readonly")
            
            ps['values'] = (15, 30, 50)
            ps.config(state="readonly")

    def generuj_mape():
        global mapsgen
        if random_enabled.get() == 1:
            s.set(random.randint(1, 9))
            
            s1.set(random.choice([7, 8, 9, 10, 11, 12, 13, 14]))
            
            hp.set(random.choice([39, 60, 100]))
            
            ps.set(random.choice([15, 30, 50]))


        gr = uczestnicy.Gracz()
        mapa_odkryta.delete(1.0, END)
        maps = Mapa(map_size)
        maps.przygotuj_mape(map_size)
        mapsgen = maps
        maps.mapa[0][0] = gr
    
        for i in range(len(maps.mapa[0])):
            for j in range(len(maps.mapa[0])):
                try:
                    if maps.mapa[i][j].otwarty:
                        if i == len(maps.mapa[0]) - 1 and j == len(maps.mapa[0]) - 1:
                            mapa_odkryta.insert(END, 'X\n')
                        elif j == len(maps.mapa[0]) - 1:
                            mapa_odkryta.insert(END, '_\n')
                        else:
                            if j == 0:
                                mapa_odkryta.insert(END, '_')
                            else:
                                mapa_odkryta.insert(END, '_')
                    elif not maps.mapa[i][j].otwarty:
                        if j == len(maps.mapa[0]) - 1:
                            mapa_odkryta.insert(END, '#\n')
                        else:
                            if j == 0:
                                mapa_odkryta.insert(END, '#')
                            else:
                                mapa_odkryta.insert(END, '#')
                    else:
                        if j == len(maps.mapa[0]) - 1:
                            mapa_odkryta.insert(END, ' \n')
                        else:
                            if j == 0:
                                mapa_odkryta.insert(END, ' ')
                            else:
                                mapa_odkryta.insert(END, ' ')
                except:
                    if j == len(maps.mapa[0]) - 1:
                        mapa_odkryta.insert(END, '8\n')
                    else:
                        if j == 0:
                            mapa_odkryta.insert(END, '8')
                        else:
                            mapa_odkryta.insert(END, '8')            
                   
    window = Tk()
    global NR_OF_LVL_GEN

    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_RESOLUTION)

    f = LabelFrame(window, text='GENERATED MAP', labelanchor='n')
    f.grid(columnspan=3, row=0)

    f2 = LabelFrame(window, text='DUNGEON OPTIONS', labelanchor='n')
    f2.grid(column=6, row=0)

    w = Label(f2, text="Dungeon level  ")
    w.grid(column=1, row=2)

    random_enabled = IntVar()
    random_enabled.set(0)
    c = Checkbutton(window, text='Randomize all parameters', variable=random_enabled, command=losuj)
    c.grid(column=6, row=3)

    NR_OF_LVL_GEN = IntVar()
    NR_OF_LVL_GEN.set(1)
    s = ttk.Combobox(f2, width=7, textvariable=NR_OF_LVL_GEN, state="readonly")
    s['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    s.grid(column=2, row=2)

    w1 = Label(f2, text="Map size  ")
    w1.grid(column=1, row=3)

    map_size = IntVar()
    map_size.set(7)
    s1 = ttk.Combobox(f2, width=7, textvariable=map_size, state='readonly')
    s1['values'] = (7, 8, 9, 10, 11, 12, 13, 14)
    s1.grid(column=2, row=3)

    w2 = Label(f2, text="Hero Life  ")
    w2.grid(column=1, row=4)

    hit_points = IntVar()
    hit_points.set(39)
    hp = ttk.Combobox(f2, width=7, textvariable=hit_points, state='readonly')
    hp['values'] = (39, 60, 100)
    hp.grid(column=2, row=4)
    
    
    w3 = Label(f2, text="Hero Strenght ")
    w3.grid(column=1, row=5)
    
    sila = IntVar()
    sila.set(15)
    ps = ttk.Combobox(f2, width=7, textvariable=sila, state='readonly')
    ps['values'] = (15, 30, 50)
    ps.grid(column=2, row=5)

    mapa_odkryta = Text(f, font=('Times', '12'), width=17, height=12)
    mapa_odkryta.grid()

    b1 = Button(window, text='GENERATE', bd=4, width=15, height=2, command=generuj_mape)
    b1.grid(column=5, row=2)

    b2 = Button(window, text='SAVE MAP', bd=4, width=15, height=2, command=lambda: zapisz_mape(mapa_odkryta))
    b2.grid(column=5, row=3)

    b3 = Button(window, text='PLAY', bd=4, width=15, height=2, bg="light blue", command=lambda: zagraj(NR_OF_LVL_GEN, map_size, hit_points, sila, window))
    b3.grid(column=6, row=2)

    b4 = Button(window, text='EXIT', bd=8, width=20, height=5, command=lambda: wyjdz(window))
    b4.grid(column=7, row=7)

    b5 = Button(window, text='LOAD MAP', bd=5, width=20, height=2, command=lambda: wczytaj_mape(mapa_odkryta))
    b5.grid(column=2, row=2)


    window.mainloop()


if __name__ == "__main__":
    generator()