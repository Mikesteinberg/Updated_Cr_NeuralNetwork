#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:19:04 2018

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
                    
with open('Card_Data.json') as card_data:
    data = json.load(card_data)
    
current_card = 0
knight = Card(data['troop'][current_card]['name'], data['troop'][0]['id'], 
      data['troop'][current_card]['elixir'], False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)

knight.print_all_data()
current_card = 1

Archer = Card(data['troop'][current_card]['name'], 26000001, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Archer.print_all_data()

current_card = 2
Goblins = Card(data['troop'][current_card]['name'], 26000002, 
      2, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Goblins.print_all_data()

current_card = 3
Giant = Card(data['troop'][current_card]['name'], 26000003, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Giant.print_all_data()

current_card = 4
Pekka = Card(data['troop'][current_card]['name'], 26000004, 
      7, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Pekka.print_all_data()

current_card = 5
Minions = Card('Minions', 26000005, 
      3, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Minions.print_all_data()

current_card = 6
Balloon = Card(data['troop'][current_card]['name'], data['troop'][current_card]['id'], 
      data['troop'][current_card]['elixir'], True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Balloon.print_all_data()

current_card = 7
Witch = Card(data['troop'][current_card]['name'], data['troop'][current_card]['id'], 
      data['troop'][current_card]['elixir'], False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=True)
Witch.print_all_data()

current_card = 9
Barbarians = Card('Barbarians', 26000008, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Barbarians.print_all_data()

current_card = 10
Golem = Card(data['troop'][current_card]['name'], 26000009, 
      8, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=True)
Golem.print_all_data()

current_card = 8
Skeletons = Card('Skeletons', 26000010, 
      1, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Skeletons.print_all_data()

current_card = 12
Valkyrie = Card(data['troop'][current_card]['name'], 26000011, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Valkyrie.print_all_data()

current_card = 13
Bomber = Card(data['troop'][current_card]['name'], data['troop'][current_card]['id'], 
      data['troop'][current_card]['elixir'], False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Bomber.print_all_data()

current_card = 14
Musketeer = Card(data['troop'][current_card]['name'], data['troop'][current_card]['id'], 
      data['troop'][current_card]['elixir'], False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Musketeer.print_all_data()

current_card = 15
Baby_Dragon = Card('Baby Dragon', 26000015, 
      4, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Baby_Dragon.print_all_data()

current_card = 16
Mini_Pekka = Card('Mini Pekka', 26000018, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Mini_Pekka.print_all_data()

current_card = 17
Wizard = Card(data['troop'][current_card]['name'], 26000017, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Wizard.print_all_data()

current_card = 18
Prince = Card(data['troop'][current_card]['name'], 26000016, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Prince.print_all_data()

current_card = 19
Spear_Goblins = Card('Spear Goblins', 26000019, 
      2, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Spear_Goblins.print_all_data()

current_card = 20
Giant_Skeleton = Card('Giant Skeleton', 26000020, 
      6, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=True)
Giant_Skeleton.print_all_data()

current_card = 21
Hog_Rider = Card('Hog Rider', 26000021, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Hog_Rider.print_all_data()

current_card = 23
Ice_Wizard = Card('Ice Wizard', 26000023, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Ice_Wizard.print_all_data()

current_card = 24
Royal_Giant = Card('Royal Giant', 26000024, 
      6, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Royal_Giant.print_all_data()

current_card = 25
Princess = Card(data['troop'][current_card]['name'], 26000026, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Princess.print_all_data()

current_card = 26
Dark_Prince = Card('Dark Prince', 26000027, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Dark_Prince.print_all_data()

current_card = 27
Guards = Card('Guards', 26000025, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Guards.print_all_data()

current_card = 28
Lava_Hound = Card('Lava Hound', 26000029, 
      7, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Lava_Hound.print_all_data()

current_card = 30
Lumberjack = Card('Lumberjack', 26000035, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Lumberjack.print_all_data()

current_card = 31
Ice_Spirit = Card('Ice Spirit', 26000030, 
      1, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Ice_Spirit.print_all_data()

current_card = 32
Fire_Spirits = Card('Fire Spirits', 26000031, 
      2, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Fire_Spirits.print_all_data()

current_card = 33
Miner = Card(data['troop'][current_card]['name'], 26000032, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Miner.print_all_data()

current_card = 34
Sparky = Card(data['troop'][current_card]['name_en'], 26000033, 
      6, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Sparky.print_all_data()

current_card = 35
Bowler = Card(data['troop'][current_card]['name_en'], 26000034, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Bowler.print_all_data()

current_card = 37
Mega_Minion = Card(data['troop'][current_card]['name_en'], 26000039, 
      3, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Mega_Minion.print_all_data()

current_card = 38
Inferno_Dragon = Card(data['troop'][current_card]['name_en'], 26000037, 
      4, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Inferno_Dragon.print_all_data()

current_card = 39
Battle_Ram = Card(data['troop'][current_card]['name_en'], 26000036, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Battle_Ram.print_all_data()

current_card = 40
Dart_Goblin = Card('Dart Goblin', 26000040, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Dart_Goblin.print_all_data()

current_card = 41
Electro_Wizard = Card(data['troop'][current_card]['name_en'], 26000042, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=True)
Electro_Wizard.print_all_data()

current_card = 42
Elite_Barbarians = Card('Elite Barbarians', 26000043, 
      6, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Elite_Barbarians.print_all_data()

current_card = 43
Executioner = Card(data['troop'][current_card]['name_en'], 26000045, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Executioner.print_all_data()

current_card = 44
Bandit = Card(data['troop'][current_card]['name_en'], 26000046, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Bandit.print_all_data()

current_card = 45
Royal_Ghost = Card(data['troop'][current_card]['name_en'], 26000050, 
      3, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Royal_Ghost.print_all_data()

current_card = 47
Zappies = Card(data['troop'][current_card]['name_en'], 26000052, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Zappies.print_all_data()

current_card = 48
Hunter = Card(data['troop'][current_card]['name_en'], 26000044, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Hunter.print_all_data()

current_card = 49
Night_Witch = Card(data['troop'][current_card]['name_en'], 26000048, 
      4, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Night_Witch.print_all_data()

current_card = 50
Bats = Card('Bats', 26000049, 
      2, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Bats.print_all_data()

current_card = 51
Cannon_Cart = Card(data['troop'][current_card]['name_en'], 26000054, 
      5, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Cannon_Cart.print_all_data()

current_card = 53
Mega_Knight = Card(data['troop'][current_card]['name_en'], 26000055, 
      7, False, True, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=True, point_damage=False)
Mega_Knight.print_all_data()

current_card = 54
Skeleton_Barrel = Card('Skeleton Barrel', 26000056, 
      3, True, False, 
      data['troop'][current_card]['attacks_air'], 
      data['troop'][current_card]['attacks_ground'], 
      data['troop'][current_card]['target_only_buildings'], True, False, False,
      splash_damage=False, point_damage=True)
Skeleton_Barrel.print_all_data()

current_card = 0
Rage = Card(data['spell'][current_card]['name'], 28000002, 
      2, False, False, 
      False, 
      False, 
      False, False, True, False,
      splash_damage=False, point_damage=False)
Rage.print_all_data()

current_card = 1
Freeze = Card(data['spell'][current_card]['name'], 28000005, 
      4, False, False, 
      False, 
      False, 
      False, False, True, False,
      splash_damage=False, point_damage=False)
Freeze.print_all_data()

current_card = 2
Lightning = Card(data['spell'][current_card]['name'], 28000007, 
      6, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=False, point_damage=True)
Lightning.print_all_data()

current_card = 3
Zap = Card(data['spell'][current_card]['name'], 28000008, 
      2, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Zap.print_all_data()

current_card = 4
Poison = Card(data['spell'][current_card]['name'], 28000009, 
      4, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Poison.print_all_data()

current_card = 6
Graveyard = Card(data['spell'][current_card]['name'], 28000010, 
      5, False, False, 
      False, 
      True, 
      False, False, True, False,
      splash_damage=False, point_damage=True)
Graveyard.print_all_data()

current_card = 8
Tornado = Card(data['spell'][current_card]['name'], 28000012, 
      3, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Tornado.print_all_data()

current_card = 9
Clone = Card(data['spell'][current_card]['name'], 28000013, 
      3, False, False, 
      False, 
      False, 
      False, False, True, False,
      splash_damage=False, point_damage=False)
Clone.print_all_data()

current_card = 10
Heal = Card('Heal', 28000016, 
      3, False, False, 
      False, 
      False, 
      False, False, True, False,
      splash_damage=False, point_damage=False)
Heal.print_all_data()

current_card = 12
Log = Card('Log', 28000011, 
      3, False, False, 
      False, 
      False, 
      False, False, True, False,
      splash_damage=True, point_damage=False,)
Log.print_all_data()

current_card = 11
Mirror = Card('Mirror', 28000006, 
      3, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=True)
Mirror.print_all_data()

Rocket = Card('Rocket', 28000003, 
      6, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Rocket.print_all_data()

Fireball = Card('Fireball', 28000000, 
      4, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Fireball.print_all_data()

Arrows = Card('Arrows', 28000001, 
      3, False, False, 
      True, 
      True, 
      False, False, True, False,
      splash_damage=True, point_damage=False)
Arrows.print_all_data()

current_card = 2
Cannon = Card(data['building'][current_card]['name'], 27000000, 
      3, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Cannon.print_all_data()

current_card = 3
Goblin_Hut = Card(data['building'][current_card]['name_en'], 27000001, 
      5, False, True, 
      True, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Goblin_Hut.print_all_data()

current_card = 4
Mortar = Card(data['building'][current_card]['name_en'], 27000002, 
      4, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=True, point_damage=False)
Mortar.print_all_data()

current_card = 5
Inferno_Tower = Card(data['building'][current_card]['name_en'], 27000003, 
      5, False, True, 
      True, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Inferno_Tower.print_all_data()

current_card = 6
Bomb_Tower = Card(data['building'][current_card]['name_en'], 27000004, 
      5, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=True, point_damage=False)
Bomb_Tower.print_all_data()

current_card = 7
Barbarian_Hut = Card(data['building'][current_card]['name_en'], 27000005, 
      7, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Barbarian_Hut.print_all_data()

current_card = 8
Tesla = Card(data['building'][current_card]['name_en'], 27000006, 
      4, False, True, 
      True, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Tesla.print_all_data()

current_card = 9
Elixir_Pump = Card(data['building'][current_card]['name_en'], 27000007, 
      6, False, True, 
      False, 
      False, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=False)
Elixir_Pump.print_all_data()

current_card = 10
X_Bow = Card(data['building'][current_card]['name_en'], 27000008, 
      6, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
X_Bow.print_all_data()

current_card = 11
Tombstone = Card(data['building'][current_card]['name_en'], 27000009, 
      3, False, True, 
      False, 
      True, 
      False, False, False, is_building=True,
      splash_damage=False, point_damage=True)
Tombstone.print_all_data()

current_card = 14
Furnace = Card(data['building'][current_card]['name_en'], 27000010, 
      4, False, True, 
      True, 
      True, 
      False, False, False, is_building=True,
      splash_damage=True, point_damage=False)
Furnace.print_all_data()

Skeleton_Army = Card('Skeleton Army', 26000012, 
      3, False, True, 
      False, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Skeleton_Army.print_all_data()

Minion_Horde = Card('Minion_Horde', 26000022, 
      5, True, False, 
      True, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Minion_Horde.print_all_data()

Three_Musketeers = Card('Three Musketeers', 26000028, 
      9, False, True, 
      True, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Three_Musketeers.print_all_data()

Ice_Golem = Card('Ice Golem', 26000038, 
      2, False, True, 
      True, 
      True, 
      True, True, False, is_building=False,
      splash_damage=True, point_damage=True)
Ice_Golem.print_all_data()

Goblin_Gang = Card('Goblin Gang', 26000041, 
      3, False, True, 
      True, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Goblin_Gang.print_all_data()

Flying_Machine = Card('Flying Machine', 26000057, 
      4, True, False, 
      True, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Flying_Machine.print_all_data()

Magic_Archer = Card('Magic_Archer', 26000062, 
      4, False, True, 
      True, 
      True, 
      False, True, False, is_building=False,
      splash_damage=True, point_damage=False)
Magic_Archer.print_all_data()

Goblin_Barrel = Card('Goblin_barrel', 28000004, 
      3, False, True, 
      False, 
      True, 
      False, True, False, is_building=False,
      splash_damage=False, point_damage=True)
Goblin_Barrel.print_all_data()