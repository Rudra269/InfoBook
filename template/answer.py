#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:30:26 2021

@author: rroy
"""
"""from aocd import get_data, submit"""
import timeit
def day2(tab) :
    

    valid = 0
    for line in tab:
        
        min_max, letter, password = line.split(' ')
        min, max = min_max.split("-")
        letter = letter[0]
    
        if password.count(letter) in range(int(min), int(max)+1):
            valid = valid + 1
    return valid


def day2_2(tab) :
    valid = 0
    for line in tab:
        
        min_max, letter, password = line.split(' ')
        min, max = min_max.split("-")
        letter = letter[0]
    
        if (password[int(min)-1]==letter) != (password[int(max)-1])==letter:
            valid = valid + 1
    return valid

def day3 (slope, right, down) :
    width = len(slope[0])
    height = len(slope)
    count = 0
    y = right
    for x in range(down, height, down):
        if slope[x][y] == "#":
            count+=1    
        y = (y+right) % width
    return count


tab = open('liste4.txt', 'r')

with open ('liste4.txt') as file:
    passports = file.read().split('\n\n')
part1, part2 = 0, 0
for p in passports:
    d = dict(x.split(':') for x in p.replace("\n", " ").split(" "))
    
