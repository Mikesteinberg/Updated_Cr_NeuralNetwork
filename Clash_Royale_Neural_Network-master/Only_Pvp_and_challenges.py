#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:11:16 2018

@author: mike
"""
import requests
import re
import time

data_file = open("match_file_magic_archer.txt", "w")
tag_file = open("nonProcessedTags.txt", "r")
playerTags = tag_file.read()
final_player_tags = playerTags.split(",")
tag_file.close()


    
tag = "9POQGR2P2"
url = "http://api.cr-api.com/player/%s" % tag

headers = {
        'auth': "14fbcc90e3f64b49b36236af89a2fd90ef3f477672d34fad837f3940d4d21ffd"
    }
        

response = requests.request("GET", url, headers=headers)


try:
    data = response.json()
except:
    print(response)
    print("")
            
for match in range (0, 25):
    match_type = data['battles'][match]["challengeType"]
    print(match_type)

