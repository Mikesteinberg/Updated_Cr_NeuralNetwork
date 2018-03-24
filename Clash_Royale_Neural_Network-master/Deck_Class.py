#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:49:01 2018

@author: mike
"""

class Deck():
    cards = []
    card_names = []
    total_elixir = 0
    total_air_cards = 0
    total_ground_cards = 0
    total_attacks_air = 0
    total_attacks_ground = 0
    total_targets_buildings = 0
    total_troops = 0
    total_spells = 0
    total_buildings = 0
    total_splash_damage = 0
    total_point_damage = 0
    
    def get_total_elixir(self):
        deck_total_elixir = 0
        for card in self.cards:
            deck_total_elixir = deck_total_elixir + card.get_elixir()
        average_elixir = (deck_total_elixir / 8)
        normalized_elixir = ((average_elixir - 1.875) / (7.125 - 1.875))
        return(normalized_elixir)
        
    def get_total_air_cards(self):
        deck_total_air_cards = 0
        for card in self.cards:
            deck_total_air_cards = deck_total_air_cards + int(card.get_air_card())
        normalized_air_cards = ((deck_total_air_cards) / (8))
        return(normalized_air_cards)
        
    def get_total_ground_cards(self):
        deck_total_ground_cards = 0
        for card in self.cards:
            deck_total_ground_cards = deck_total_ground_cards + int(card.get_ground_card())
        normalized_ground_cards = ((deck_total_ground_cards) / (8))
        return(normalized_ground_cards)
        
    def get_total_attacks_air(self):
        deck_total_attacks_air = 0
        for card in self.cards:
            deck_total_attacks_air = deck_total_attacks_air + int(card.get_attacks_air())
        normalized_attacks_air = ((deck_total_attacks_air) / (8))
        return(normalized_attacks_air)
        
    def get_total_attacks_ground(self):
        deck_total_attacks_ground = 0
        for card in self.cards:
            deck_total_attacks_ground = deck_total_attacks_ground + int(card.get_attacks_ground())
        normalized_attacks_ground = ((deck_total_attacks_ground) / (8))
        return(normalized_attacks_ground)
        
    def get_total_targets_buildings(self):
        deck_total_targets_buildings = 0
        for card in self.cards:
            deck_total_targets_buildings = deck_total_targets_buildings + int(card.get_target_builings())
        normalized_targets_buildings = ((deck_total_targets_buildings) / (8))
        return(normalized_targets_buildings)
        
    def get_total_troops(self):
        deck_total_troops = 0
        for card in self.cards:
            deck_total_troops = deck_total_troops + int(card.get_is_troop())
        normalized_troops = ((deck_total_troops) / (8))
        return(normalized_troops)
        
    def get_total_buildings(self):
        deck_total_buildings = 0
        for card in self.cards:
            deck_total_buildings = deck_total_buildings + int(card.get_is_building())
        normalized_buildings = ((deck_total_buildings) / (8))
        return(normalized_buildings)
    def get_total_spells(self):
        deck_total_spells = 0
        for card in self.cards:
            deck_total_spells = deck_total_spells + int(card.get_is_spell())
        normalized_spells = ((deck_total_spells) / (8))
        return(normalized_spells)

    def get_total_splash_damage(self):
        deck_total_splash_damage = 0
        for card in self.cards:
            deck_total_splash_damage = deck_total_splash_damage + int(card.get_splash_damage())
        normalized_splash = ((deck_total_splash_damage) / (8))
        return(normalized_splash)
        
    def get_total_point_damage(self):
        deck_total_point_damage = 0
        for card in self.cards:
            deck_total_point_damage = deck_total_point_damage + int(card.get_point_damage())
        normalized_point = ((deck_total_point_damage) / (8))
        return(normalized_point)
        
    def set_card_names(self, cards):
        card_array = []
        for card in cards:
            card_array.append(card.get_name())
        return(card_array)
        
    def get_card_names(self):
        return self.card_names
    
    def get_link_array(self):
        link_array = []
        for card in self.cards:
            link_array.append(inv_map[card])
        return(link_array)
                    
    def __init__(self, cards):
        self.card_names = self.set_card_names(cards)
        self.cards = cards
