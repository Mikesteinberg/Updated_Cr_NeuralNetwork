#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:00:07 2018

@author: mike
"""
import json
import numpy as np
from keras.models import load_model
ladder_model = load_model("new_ladder_model.h5")

#deck1 = ['26000021', '26000045', '28000012', '26000002', '26000000', '28000003', '28000011', '26000030']
#deck2 = ['26000029', '26000025', '26000006', '26000005', '26000039', '27000009', '28000008', '28000000']
def build_match_arrays(first_deck, second_deck):
    from Card_Class import Card
    
    with open('Card_Data.json') as card_data:
        data = json.load(card_data)
        
    current_card = 0
    Knight = Card(data['troop'][current_card]['name'], data['troop'][0]['id'], 
          data['troop'][current_card]['elixir'], False, True, 
          data['troop'][current_card]['attacks_air'], 
          data['troop'][current_card]['attacks_ground'], 
          data['troop'][current_card]['target_only_buildings'], True, False, False,
          splash_damage=False, point_damage=True)
    
    Knight.print_all_data()
    current_card = 1
    
    Archers = Card(data['troop'][current_card]['name'], 26000001, 
          3, False, True, 
          data['troop'][current_card]['attacks_air'], 
          data['troop'][current_card]['attacks_ground'], 
          data['troop'][current_card]['target_only_buildings'], True, False, False,
          splash_damage=False, point_damage=True)
    Archers.print_all_data()
    
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
          True, 
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
          splash_damage=True, point_damage=True)
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
          2, False, False, 
          False, 
          True, 
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
    
    Magic_Archer = Card('Magic Archer', 26000062, 
          4, False, True, 
          True, 
          True, 
          False, True, False, is_building=False,
          splash_damage=True, point_damage=False)
    Magic_Archer.print_all_data()
    
    Goblin_Barrel = Card('Goblin Barrel', 28000004, 
          3, False, True, 
          False, 
          True, 
          False, True, False, is_building=False,
          splash_damage=False, point_damage=True)
    Goblin_Barrel.print_all_data()
    
    Not_Available = Card('Not_Available', 0, 
          3, False, True, 
          False, 
          True, 
          False, True, False, is_building=False,
          splash_damage=False, point_damage=True)
    Not_Available.print_all_data()
    
    card_links = {}
    card_links["26000000"] = Knight
    card_links["26000001"] = Archers
    card_links["26000002"] = Goblins
    card_links["26000003"] = Giant
    card_links["26000004"] = Pekka
    card_links["26000005"] = Minions
    card_links["26000006"] = Balloon
    card_links["26000007"] = Witch
    card_links["26000008"] = Barbarians
    card_links["26000009"] = Golem
    card_links["26000010"] = Skeletons
    card_links["26000011"] = Valkyrie
    card_links["26000012"] = Skeleton_Army
    card_links["26000013"] = Bomber
    card_links["26000014"] = Musketeer
    card_links["26000015"] = Baby_Dragon
    card_links["26000016"] = Prince
    card_links["26000017"] = Wizard
    card_links["26000018"] = Mini_Pekka
    card_links["26000019"] = Spear_Goblins
    card_links["26000020"] = Giant_Skeleton
    card_links["26000021"] = Hog_Rider
    card_links["26000022"] = Minion_Horde
    card_links["26000023"] = Ice_Wizard
    card_links["26000024"] = Royal_Giant
    card_links["26000025"] = Guards
    card_links["26000026"] = Princess
    card_links["26000027"] = Dark_Prince
    card_links["26000028"] = Three_Musketeers
    card_links["26000029"] = Lava_Hound
    card_links["26000030"] = Ice_Spirit
    card_links["26000031"] = Fire_Spirits
    card_links["26000032"] = Miner
    card_links["26000033"] = Sparky
    card_links["26000034"] = Bowler
    card_links["26000035"] = Lumberjack
    card_links["26000036"] = Battle_Ram
    card_links["26000037"] = Inferno_Dragon
    card_links["26000038"] = Ice_Golem
    card_links["26000039"] = Mega_Minion
    card_links["26000040"] = Dart_Goblin
    card_links["26000041"] = Goblin_Gang
    card_links["26000042"] = Electro_Wizard
    card_links["26000043"] = Elite_Barbarians
    card_links["26000044"] = Hunter
    card_links["26000045"] = Executioner
    card_links["26000046"] = Bandit
    card_links["26000048"] = Night_Witch
    card_links["26000049"] = Bats
    card_links["26000050"] = Royal_Ghost
    card_links["26000052"] = Zappies
    card_links["26000054"] = Cannon_Cart
    card_links["26000055"] = Mega_Knight
    card_links["26000056"] = Skeleton_Barrel
    card_links["26000057"] = Flying_Machine
    card_links["26000062"] = Magic_Archer
    card_links["27000000"] = Cannon
    card_links["27000001"] = Goblin_Hut
    card_links["27000002"] = Mortar
    card_links["27000003"] = Inferno_Tower
    card_links["27000004"] = Bomb_Tower
    card_links["27000005"] = Barbarian_Hut
    card_links["27000006"] = Tesla
    card_links["27000007"] = Elixir_Pump
    card_links["27000008"] = X_Bow
    card_links["27000009"] = Tombstone
    card_links["27000010"] = Furnace
    card_links["28000000"] = Fireball
    card_links["28000001"] = Arrows
    card_links["28000002"] = Rage
    card_links["28000003"] = Rocket
    card_links["28000004"] = Goblin_Barrel
    card_links["28000005"] = Freeze
    card_links["28000006"] = Mirror
    card_links["28000007"] = Lightning
    card_links["28000008"] = Zap
    card_links["28000009"] = Poison
    card_links["28000010"] = Graveyard
    card_links["28000011"] = Log
    card_links["28000012"] = Tornado
    card_links["28000013"] = Clone
    card_links["28000016"] = Heal
    card_links["26000062"] = Magic_Archer
    card_links["n/a"] = Not_Available
    
    
    
    deck_one_list = []
    for link in first_deck:
        deck_one_list.append(card_links[link])
        
    
    deck_two_list = []
    for link in second_deck:
        deck_two_list.append(card_links[link])
        
    from Deck_Class import Deck
    
    deck_one = Deck(deck_one_list)
    deck_two = Deck(deck_two_list)
    
    print(deck_one.get_card_names())
    print(deck_two.get_card_names())
    
    card_hot_encoder = {}
    card_hot_encoder["26000000"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    card_hot_encoder["26000001"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000000010"
    card_hot_encoder["26000002"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000000100"
    card_hot_encoder["26000003"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000001000"
    card_hot_encoder["26000004"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000010000"
    card_hot_encoder["26000005"] = "100000000000000000000000000000000000000000000000000000000000000000000000000000100000"
    card_hot_encoder["26000006"] = "100000000000000000000000000000000000000000000000000000000000000000000000000001000000"
    card_hot_encoder["26000007"] = "100000000000000000000000000000000000000000000000000000000000000000000000000010000000"
    card_hot_encoder["26000008"] = "100000000000000000000000000000000000000000000000000000000000000000000000000100000000"
    card_hot_encoder["26000009"] = "100000000000000000000000000000000000000000000000000000000000000000000000001000000000"
    card_hot_encoder["26000010"] = "100000000000000000000000000000000000000000000000000000000000000000000000010000000000"
    card_hot_encoder["26000011"] = "100000000000000000000000000000000000000000000000000000000000000000000000100000000000"
    card_hot_encoder["26000012"] = "100000000000000000000000000000000000000000000000000000000000000000000001000000000000"
    card_hot_encoder["26000013"] = "100000000000000000000000000000000000000000000000000000000000000000000010000000000000"
    card_hot_encoder["26000014"] = "100000000000000000000000000000000000000000000000000000000000000000000100000000000000"
    card_hot_encoder["26000015"] = "100000000000000000000000000000000000000000000000000000000000000000001000000000000000"
    card_hot_encoder["26000016"] = "100000000000000000000000000000000000000000000000000000000000000000010000000000000000"
    card_hot_encoder["26000017"] = "100000000000000000000000000000000000000000000000000000000000000000100000000000000000"
    card_hot_encoder["26000018"] = "100000000000000000000000000000000000000000000000000000000000000001000000000000000000"
    card_hot_encoder["26000019"] = "100000000000000000000000000000000000000000000000000000000000000010000000000000000000"
    card_hot_encoder["26000020"] = "100000000000000000000000000000000000000000000000000000000000000100000000000000000000"
    card_hot_encoder["26000021"] = "100000000000000000000000000000000000000000000000000000000000001000000000000000000000"
    card_hot_encoder["26000022"] = "100000000000000000000000000000000000000000000000000000000000010000000000000000000000"
    card_hot_encoder["26000023"] = "100000000000000000000000000000000000000000000000000000000000100000000000000000000000"
    card_hot_encoder["26000024"] = "100000000000000000000000000000000000000000000000000000000001000000000000000000000000"
    card_hot_encoder["26000025"] = "100000000000000000000000000000000000000000000000000000000010000000000000000000000000"
    card_hot_encoder["26000026"] = "100000000000000000000000000000000000000000000000000000000100000000000000000000000000"
    card_hot_encoder["26000027"] = "100000000000000000000000000000000000000000000000000000001000000000000000000000000000"
    card_hot_encoder["26000028"] = "100000000000000000000000000000000000000000000000000000010000000000000000000000000000"
    card_hot_encoder["26000029"] = "100000000000000000000000000000000000000000000000000000100000000000000000000000000000"
    card_hot_encoder["26000030"] = "100000000000000000000000000000000000000000000000000001000000000000000000000000000000"
    card_hot_encoder["26000031"] = "100000000000000000000000000000000000000000000000000010000000000000000000000000000000"
    card_hot_encoder["26000032"] = "100000000000000000000000000000000000000000000000000100000000000000000000000000000000"
    card_hot_encoder["26000033"] = "100000000000000000000000000000000000000000000000001000000000000000000000000000000000"
    card_hot_encoder["26000034"] = "100000000000000000000000000000000000000000000000010000000000000000000000000000000000"
    card_hot_encoder["26000035"] = "100000000000000000000000000000000000000000000000100000000000000000000000000000000000"
    card_hot_encoder["26000036"] = "100000000000000000000000000000000000000000000001000000000000000000000000000000000000"
    card_hot_encoder["26000037"] = "100000000000000000000000000000000000000000000010000000000000000000000000000000000000"
    card_hot_encoder["26000038"] = "100000000000000000000000000000000000000000000100000000000000000000000000000000000000"
    card_hot_encoder["26000039"] = "100000000000000000000000000000000000000000001000000000000000000000000000000000000000"
    card_hot_encoder["26000040"] = "100000000000000000000000000000000000000000010000000000000000000000000000000000000000"
    card_hot_encoder["26000041"] = "100000000000000000000000000000000000000000100000000000000000000000000000000000000000"
    card_hot_encoder["26000042"] = "100000000000000000000000000000000000000001000000000000000000000000000000000000000000"
    card_hot_encoder["26000043"] = "100000000000000000000000000000000000000010000000000000000000000000000000000000000000"
    card_hot_encoder["26000044"] = "100000000000000000000000000000000000000100000000000000000000000000000000000000000000"
    card_hot_encoder["26000045"] = "100000000000000000000000000000000000001000000000000000000000000000000000000000000000"
    card_hot_encoder["26000046"] = "100000000000000000000000000000000000010000000000000000000000000000000000000000000000"
    card_hot_encoder["26000048"] = "100000000000000000000000000000000000100000000000000000000000000000000000000000000000"
    card_hot_encoder["26000049"] = "100000000000000000000000000000000001000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000050"] = "100000000000000000000000000000000010000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000052"] = "100000000000000000000000000000000100000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000054"] = "100000000000000000000000000000001000000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000055"] = "100000000000000000000000000000010000000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000056"] = "100000000000000000000000000000100000000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000057"] = "100000000000000000000000000001000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000000"] = "100000000000000000000000000010000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000001"] = "100000000000000000000000000100000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000002"] = "100000000000000000000000001000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000003"] = "100000000000000000000000010000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000004"] = "100000000000000000000000100000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000005"] = "100000000000000000000001000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000006"] = "100000000000000000000010000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000007"] = "100000000000000000000100000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000008"] = "100000000000000000001000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000009"] = "100000000000000000010000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["27000010"] = "100000000000000000100000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000000"] = "100000000000000001000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000001"] = "100000000000000010000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000002"] = "100000000000000100000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000003"] = "100000000000001000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000004"] = "100000000000010000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000005"] = "100000000000100000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000006"] = "100000000001000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000007"] = "100000000010000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000008"] = "100000000100000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000009"] = "100000001000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000010"] = "100000010000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000011"] = "100000100000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000012"] = "100001000000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000013"] = "100010000000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["28000016"] = "100100000000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["26000062"] = "101000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["n/a"] =      "110000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    card_hot_encoder["n/a).join(';')}"] = "110000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        
    deck_one_encoded_cards = []
    for link in first_deck:
        deck_one_encoded_cards.append(card_hot_encoder[link])
        
    deck_two_encoded_cards = []
    for link in second_deck:
        deck_two_encoded_cards.append(card_hot_encoder[link])
        
    def create_deck_string(card_array):
        deck_sum = 0
        for card in card_array:
            card_value = int(card)
            deck_sum = deck_sum + card_value
        deck_string = str(deck_sum)
        return deck_string[1:]
    
    encoded_deck_one = create_deck_string(deck_one_encoded_cards)
    
    encoded_deck_one_array = []
    for char in encoded_deck_one:
        encoded_deck_one_array.append(char)
    
    encoded_deck_two = create_deck_string(deck_two_encoded_cards)
    
    encoded_deck_two_array = []
    for char in encoded_deck_two:
        encoded_deck_two_array.append(char)
    
    #print(encoded_deck_one)
    #print(encoded_deck_two)
    
    first_deck_stats_array = []
    first_deck_stats_array.append(deck_one.get_total_elixir())
    first_deck_stats_array.append(deck_one.get_total_air_cards())
    first_deck_stats_array.append(deck_one.get_total_ground_cards())
    first_deck_stats_array.append(deck_one.get_total_attacks_air())
    first_deck_stats_array.append(deck_one.get_total_attacks_ground())
    first_deck_stats_array.append(deck_one.get_total_targets_buildings())
    first_deck_stats_array.append(deck_one.get_total_troops())
    first_deck_stats_array.append(deck_one.get_total_buildings())
    first_deck_stats_array.append(deck_one.get_total_spells())
    first_deck_stats_array.append(deck_one.get_total_splash_damage())
    first_deck_stats_array.append(deck_one.get_total_point_damage())
    
    #print(first_deck_stats_array)
    
    second_deck_stats_array = []
    second_deck_stats_array.append(deck_two.get_total_elixir())
    second_deck_stats_array.append(deck_two.get_total_air_cards())
    second_deck_stats_array.append(deck_two.get_total_ground_cards())
    second_deck_stats_array.append(deck_two.get_total_attacks_air())
    second_deck_stats_array.append(deck_two.get_total_attacks_ground())
    second_deck_stats_array.append(deck_two.get_total_targets_buildings())
    second_deck_stats_array.append(deck_two.get_total_troops())
    second_deck_stats_array.append(deck_two.get_total_buildings())
    second_deck_stats_array.append(deck_two.get_total_spells())
    second_deck_stats_array.append(deck_two.get_total_splash_damage())
    second_deck_stats_array.append(deck_two.get_total_point_damage())
    
    #print(second_deck_stats_array)
    
    match_array = []
    match_array = encoded_deck_one_array[:]
    for char in first_deck_stats_array:
        match_array.append(char)
    for char in encoded_deck_two:
        match_array.append(char)
    for char in second_deck_stats_array:
        match_array.append(char)
            
    match_array_two = []
    match_array_two = encoded_deck_two_array[:]
    for char2 in second_deck_stats_array:
        match_array_two.append(char2)
    for char2 in encoded_deck_one:
        match_array_two.append(char2)
    for char2 in first_deck_stats_array:
        match_array_two.append(char2)
    
    matches_array = [match_array, match_array_two]    
    return(matches_array)

def check_deck_matchup(tuple1,tuple2):

    tuples = tuple1
    First_Probability = ladder_model.predict(np.array([tuples]))
    tuples2 = tuple2
    Second_Probability = ladder_model.predict(np.array([tuples2]))
    Second_Probability_Reversed = np.fliplr(Second_Probability)
    total_probability = (First_Probability + Second_Probability_Reversed)/2
    
    return(total_probability) 


#matches_array_final = build_match_arrays(deck1, deck2)
#probabilites = check_deck_matchup(matches_array_final[0], matches_array_final[1])
#print(probabilites)

from flask import Flask, render_template, request, jsonify
from meinheld import server, middleware
import logging

SECRET_KEY = 'development key'
DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/calculate')
def calculate():
    decks = request.query_string.decode("utf-8")
    deck1_string = decks[6:77]
    deck2_string = decks[84:]
    deck1_array = deck1_string.split(";")
    deck2_array = deck2_string.split(";")
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.warning(deck1_string)        
    logging.warning(deck1_array)
    matches_array_final = build_match_arrays(deck1_array, deck2_array)
    logging.warning(matches_array_final)
    probabilites = check_deck_matchup(matches_array_final[0], matches_array_final[1])
    logging.warning(probabilites)
    probabilities_final_array = probabilites[0]
    logging.warning(probabilities_final_array)
    win = probabilities_final_array[0]
    tie = probabilities_final_array[1]
    loss = probabilities_final_array[2]
    logging.warning(win)
    logging.warning(tie)
    logging.warning(loss)
    json_array = {'Deck One Wins': str(win), 'Tie': str(tie), 'Deck Two Wins': str(loss)}
    return jsonify(json_array)


if __name__ == "__main__":
    server.listen(("0.0.0.0", 8000))
    server.run(middleware.WebSocketMiddleware(app))
'''
from bottle import run, get, request
import logging


@get('/calculate')
def calculate():
    decks = request.query_string
    deck1_string = decks[6:77]
    deck2_string = decks[84:]
    deck1_array = deck1_string.split(";")
    deck2_array = deck2_string.split(";")
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.warning(deck1_string)        
    logging.warning(deck1_array)
    matches_array_final = build_match_arrays(deck1_array, deck2_array)
    logging.warning(matches_array_final)
    probabilites = check_deck_matchup(matches_array_final[0], matches_array_final[1])
    logging.warning(probabilites)
    probabilities_final_array = probabilites[0]
    logging.warning(probabilities_final_array)
    win = probabilities_final_array[0]
    tie = probabilities_final_array[1]
    loss = probabilities_final_array[2]
    logging.warning(win)
    logging.warning(tie)
    logging.warning(loss)
    json_array = {'Deck One Wins': str(win), 'Tie': str(tie), 'Deck Two Wins': str(loss)}
    return json_array

server.listen(("192.168.1.22", 8080))
server.run
'''
    



