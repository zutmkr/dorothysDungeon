# -*- coding: utf-8 -*-
import random
import podziemia

stuff = ['sword', 'armor', 'potion', 'shoes', 'crossbow', 'tiara', 'ring', 'amulet', 'shield', 'belt', 'gloves', 'pet']
dobry_prefix = ['good', 'magic', 'rare', 'legendary']
zly_prefix = ['common', 'broken', 'rusty', 'cursed']


class Przedmiot:
    def __init__(self):
        self.nazwa = random.choice(stuff)
        self.wartosc = 50.0


class Wartosciowy:
    def dodaj_przedmiot(self):
        y = Przedmiot()
        p = random.choice(dobry_prefix)
        y.nazwa = p + ' ' + y.nazwa
        
        if p == 'good':
            y.wartosc = (y.wartosc * 1.25) * podziemia.poziom_p
        elif p == 'magic':
            y.wartosc = (y.wartosc * 1.5) * podziemia.poziom_p
        elif p == 'rare':
            y.wartosc = (y.wartosc * 1.75) * podziemia.poziom_p
        elif p == 'legendary':
            y.wartosc = (y.wartosc * 2) * podziemia.poziom_p
        return y


class Smiec:
    def dodaj_przedmiot(self):
        y = Przedmiot()
        p = random.choice(zly_prefix)
        y.nazwa = p + ' ' + y.nazwa
        
        if p == 'common':
            y.wartosc = y.wartosc * podziemia.poziom_p
        elif p == 'broken':
            y.wartosc = (y.wartosc * 0.75) * podziemia.poziom_p
        elif p == 'rusty':
            y.wartosc = (y.wartosc * 0.5) * podziemia.poziom_p
        elif p == 'cursed':
            y.wartosc = (y.wartosc * 0.25) * podziemia.poziom_p
        return y
