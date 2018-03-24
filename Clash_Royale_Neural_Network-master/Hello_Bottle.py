#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:23:14 2018

@author: mike
"""

from bottle import run, route

@route('/login')
def login():
    return '<h1> On The Login Page </h1>'

@route('/register')
def register():
    return '<h1> On The Register Page </h1>'

@route('/article/<id>')
def article(id):
    return '<h1> You are Viewing Article ' + id + '</h1>'

@route('/page/<id>/<name>')
def page(id, name):
    return '<h1> You are Viewing Article ' + id + ' With a name of ' + name + '</h1>'

@route('/posted', method='POST')
def posted():
    return '<h1> Posted </h1>'

if __name__ == '__main__':
    run(reloader = True)