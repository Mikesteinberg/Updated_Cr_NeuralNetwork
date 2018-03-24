#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:09:19 2018

@author: mike
"""
import requests

for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            try:
                url = 'http://accutech.no-ip.org:8080/calculate?deck1=2600002%s;26000044;2800001%s;26000002;26000000;28000003;28000011;26000030&deck2=26000029;26000025;26000006;26000005;26000039;2700000%s;28000008;28000000' % (i, j, k) 
                response = requests.request("GET", url)
                data = response.json()
                print(data)
            except:
                continue


