#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:48:46 2018

@author: mike
"""

card_links = {}
card_links["26000000"] = "Knight"
card_links["26000001"] = "Archers"
card_links["26000002"] = "Goblins"
card_links["26000003"] = "Giant"
card_links["26000004"] = "Pekka"
card_links["26000005"] = "Minions"
card_links["26000006"] = "Balloon"
card_links["26000007"] = "Witch"
card_links["26000008"] = "Barbarians"
card_links["26000009"] = "Golem"
card_links["26000010"] = "Skeletons"
card_links["26000011"] = "Valkyrie"
card_links["26000012"] = "Skeleton Army"
card_links["26000013"] = "Bomber"
card_links["26000014"] = "Musketeer"
card_links["26000015"] = "Baby Dragon"
card_links["26000016"] = "Prince"
card_links["26000017"] = "Wizard"
card_links["26000018"] = "Mini Pekka"
card_links["26000019"] = "Spear Goblins"
card_links["26000020"] = "Giant Skeleton"
card_links["26000021"] = "Hog Rider"
card_links["26000022"] = "Minion Horde"
card_links["26000023"] = "Ice Wizard"
card_links["26000024"] = "Royal Giant"
card_links["26000025"] = "Guards"
card_links["26000026"] = "Princess"
card_links["26000027"] = "Dark Prince"
card_links["26000028"] = "Three Musketeers"
card_links["26000029"] = "Lava Hound"
card_links["26000030"] = "Ice Spirit"
card_links["26000031"] = "Fire Spirits"
card_links["26000032"] = "Miner"
card_links["26000033"] = "Sparky"
card_links["26000034"] = "Bowler"
card_links["26000035"] = "Lumberjack"
card_links["26000036"] = "Battle Ram"
card_links["26000037"] = "Inferno Dragon"
card_links["26000038"] = "Ice Golem"
card_links["26000039"] = "Mega Minion"
card_links["26000040"] = "Dart Goblin"
card_links["26000041"] = "Goblin Gang"
card_links["26000042"] = "Electro Wizard"
card_links["26000043"] = "Elite Barbarians"
card_links["26000044"] = "Hunter"
card_links["26000045"] = "Executioner"
card_links["26000046"] = "Bandit"
card_links["26000048"] = "Night Witch"
card_links["26000049"] = "Bats"
card_links["26000050"] = "Royal Ghost"
card_links["26000052"] = "Zappies"
card_links["26000054"] = "Cannon Cart"
card_links["26000055"] = "Mega Knight"
card_links["26000056"] = "Skeleton Barrel"
card_links["26000057"] = "Flying Machine"
card_links["26000062"] = "Magic Archer"
card_links["27000000"] = "Cannon"
card_links["27000001"] = "Goblin Hut"
card_links["27000002"] = "Mortar"
card_links["27000003"] = "Inferno Tower"
card_links["27000004"] = "Bomb Tower"
card_links["27000005"] = "Barbarian Hut"
card_links["27000006"] = "Tesla"
card_links["27000007"] = "Pump"
card_links["27000008"] = "X-Bow"
card_links["27000009"] = "Tombstone"
card_links["27000010"] = "Furnace"
card_links["28000000"] = "Fireball"
card_links["28000001"] = "Arrows"
card_links["28000002"] = "Rage"
card_links["28000003"] = "Rocket"
card_links["28000004"] = "Goblin Barrel"
card_links["28000005"] = "Freeze"
card_links["28000006"] = "Mirror"
card_links["28000007"] = "Lightning"
card_links["28000008"] = "Zap"
card_links["28000009"] = "Poison"
card_links["28000010"] = "Graveyard"
card_links["28000011"] = "Log"
card_links["28000012"] = "Tornado"
card_links["28000013"] = "Clone"
card_links["28000016"] = "Heal"
card_links["26000062"] = "Magic Archer"
card_links["n/a"] = "Not Available"
    
inv_map = {v: k for k, v in card_links.items()}

first_deck = ["Hog Rider","Executioner","Tornado","Goblins","Knight","Rocket","Log","Ice Spirit"]
link_array1 = []
for card in first_deck:
    link_array1.append(inv_map[card])
    

second_deck = ["Lava Hound","Guards","Balloon","Minions","Mega Minion","Tombstone","Zap","Fireball"]
link_array2 = []
for card in second_deck:
    link_array2.append(inv_map[card])

import sys
card_number = 0
for card in link_array1:    
    sys.stdout.write(card)
    if card_number < 7:
        sys.stdout.write(';')
        card_number = card_number + 1
        
print("")
card_number = 0
for card in link_array2:    
    sys.stdout.write(card)
    if card_number < 7:
        sys.stdout.write(';')
        card_number = card_number + 1
