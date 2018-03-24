#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:32:43 2018

@author: mike
"""

import json


card_data_file = open("Card_Data.json", "r")

class Card():
    
    name= ""
    link = ""
    elixir = 0
    air_card = False
    ground_card = False
    attacks_air = False
    attacks_ground = False
    targets_buildings = False
    is_troop = False
    is_spell = False
    is_building = False
    splash_damage = False
    point_damage = False
    
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_link(self, link):
        self.link = link
    
    def get_link(self):
        return self.link
    
    def set_elixir(self, elixir):
        self.elixir = elixir
    
    def get_elixir(self):
        return self.elixir
    
    def set_air_card(self, air_card):
        self.air_card = air_card
    
    def get_air_card(self):
        return self.air_card
    
    def set_ground_card(self, ground_card):
        self.ground_card = ground_card
    
    def get_ground_card(self):
        return self.ground_card
    
    def set_attacks_air(self, attacks_air):
        self.attacks_air = attacks_air
    
    def get_attacks_air(self):
        return self.attacks_air
    
    def set_attacks_ground(self, attacks_ground):
        self.attacks_ground = attacks_ground
    
    def get_attacks_ground(self):
        return self.attacks_ground
    
    def get_target_builings(self):
        return self.targets_buildings
    
    def set_target_buildings(self, targets_buildings):
        self.targets_buildings = targets_buildings  
    
    def get_is_troop(self):
        return self.is_troop
        
    def set_is_troop(self, is_troop):
        self.is_troop = is_troop
        
    def get_is_spell(self):
        return self.is_spell
        
    def set_is_spell(self, is_spell):
        self.is_spell = is_spell
        
    def get_is_building(self):
        return self.is_building
        
    def set_is_building(self, is_building):
        self.is_building = is_building
        
    def get_splash_damage(self):
        return self.splash_damage
        
    def set_splash_damage(self, splash_damage):
        self.splash_damage = splash_damage
        
    def get_point_damage(self):
        return self.point_damage
        
    def set_point_damage(self, point_damage):
        self.point_damage = point_damage    
    
    def __init__(self, name, link, elixir, air_card, ground_card, attacks_air,
                 attacks_ground, targets_buildings, is_troop, is_spell,  
                 is_building, splash_damage, point_damage):
        self.set_name(name)
        self.set_link(link)
        self.set_elixir(elixir)
        self.set_air_card(air_card)
        self.set_ground_card(ground_card)
        self.set_attacks_air(attacks_air)
        self.set_attacks_ground(attacks_ground)
        self.set_target_buildings(targets_buildings)
        self.set_is_troop(is_troop)
        self.set_is_spell(is_spell)
        self.set_is_building(is_building)
        self.set_splash_damage(splash_damage)
        self.set_point_damage(point_damage)
     
    def print_all_data(self):
        print('''Name: {}, Id: {}, Elixir: {}, Air Card: {}, Ground Card: {}, 
        Attacks Air: {}, Attacks Ground: {}, Targets Buildings: {}, 
        Is Troop: {}, Is Spell: {}, Is Building: {}, Splash Damage: {},
        Point Damage: {}'''.format(self.name, 
              self.link, self.elixir, self.air_card, self.ground_card,
              self.attacks_air, self.attacks_ground, self.targets_buildings, 
              self.is_troop, self.is_spell, self.is_building, 
              self.splash_damage, self.point_damage))