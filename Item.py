# -*- coding: utf-8 -*-
import random
import Undergrounds

stuff = ['sword', 'armor', 'potion', 'shoes', 'crossbow', 'tiara', 'ring', 'amulet', 'shield', 'belt', 'gloves', 'pet']
good_prefix = ['good', 'magic', 'rare', 'legendary']
bad_prefix = ['common', 'broken', 'rusty', 'cursed']


class Item:
    def __init__(self):
        self.name = random.choice(stuff)
        self.value = 50.0


class Value_item:
    def Add_Item(self):
        y = Item()
        p = random.choice(good_prefix)
        y.name = p + ' ' + y.name
        
        if p == 'good':
            y.value = (y.value * 1.25) * Undergrounds.poziom_p
        elif p == 'magic':
            y.value = (y.value * 1.5) * Undergrounds.poziom_p
        elif p == 'rare':
            y.value = (y.value * 1.75) * Undergrounds.poziom_p
        elif p == 'legendary':
            y.value = (y.value * 2) * Undergrounds.poziom_p
        return y


class trash_item:
    def Add_Item(self):
        y = Item()
        p = random.choice(bad_prefix)
        y.name = p + ' ' + y.name
        
        if p == 'common':
            y.value = y.value * Undergrounds.poziom_p
        elif p == 'broken':
            y.value = (y.value * 0.75) * Undergrounds.poziom_p
        elif p == 'rusty':
            y.value = (y.value * 0.5) * Undergrounds.poziom_p
        elif p == 'cursed':
            y.value = (y.value * 0.25) * Undergrounds.poziom_p
        return y
