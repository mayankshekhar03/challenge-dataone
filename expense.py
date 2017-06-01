# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:01:30 2017

@author: Mayank Shekhar
"""


def loadWords():
    """
    csv file is loaded into a list
    """
    print("Loading csv file...")
    inFile = open('data.csv', 'r')
    shopList = []
    for line in inFile:
        shopList.append(line.strip().split(', '))
    return shopList
 
def expenseCal(shopList):
    for i in shopList:
        print(i)
    items = []
    pmatch = []
    pmatch1 = []
    items.extend(input('Enter the items:').split(' '))
    
    #generating a list of available items details
    for i in items:
        for j in shopList:
            if i in j:
                pmatch1.extend([i])
                pmatch.append([j[0],j[1],i])
    
    #if all the items are not found print none
    for i in items:
        if i not in pmatch1:
            print('none')
            input('Enter any key to exit')
            return 1
    
    #generating possible shops
    shops = []
    for i in pmatch:
        if i[0] not in shops:
            shops.extend(i[0])
    
    #removing shops which don't have all the items
    pmatch2 = pmatch[:]
    shops1 = shops[:]
    for i in shops1:
        count = 0
        for j in items:
            for k in pmatch2:
                if i == k[0] and j == k[2]:
                    count+=1
        if count != len(items):
            for l in pmatch:
                if l[0] == i:
                    pmatch.remove(l)
                    shops.remove(l[0])
    if not pmatch:
        print('none')
        input('Enter any key to exit')
        return 1
        
    #removing rendundant combo items
    pmatch3 = pmatch[:]
    for i in range(0, len(pmatch3)):
        for j in pmatch3[i+1:]:
            if pmatch3[i][0] == j[0] and pmatch3[i][1] == j[1]:
                pmatch.remove(j)
    if not pmatch:
        print('none')
        input('Enter any key to exit')
        return 1
        
    #calculating the total cost per shop
    tcost = {}
    for i in shops:
        cost = 0
        for j in pmatch:
            if i == j[0]:
                cost += float(j[1])
        tcost[i] = cost
        
    #choosing the shop providing items at the cheapest price
    min = list(tcost.values())[0]
    shop = list(tcost.keys())[0]
    for i in list(tcost.keys()):
        if min > tcost[i]:
            min = tcost[i]
            shop = i
    
    print(shop+', ', min)
    input('Enter any key to exit')
        
    
    
    
    
expenseCal(loadWords())
                
        
