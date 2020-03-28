import json
def import_items():
    dataPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\item.json'
    existingData = None
    itemCount = 0

    with open(dataPath) as f:
        existingData = json.load(f)
    itemCount = len(existingData)
    
    with open('./tools/item_add.txt') as f:
        for line in f:
            props = line.rstrip().split('|')
            existingData[props[0].lower()] = {
                "id": itemCount,
                "name": props[0].lower(),
                "price": props[1],
                "type": props[2]
            }
            itemCount += 1
    
    with open(dataPath, 'w') as f:
        json.dump(existingData, f)

def import_fish():
    fishPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\fish.json'
    itemPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\item.json'
    fishData = None
    itemData = None

    with open(itemPath) as f:
        itemData = json.load(f)
    with open(fishPath) as f:
        fishData = json.load(f)
    
    with open('./tools/fish_add.txt') as f:
        for line in f:
            props = line.rstrip().split('|')
            fishData[props[0].lower()] = {
                "id": itemData[props[0].lower()]["id"],
                "name": props[0].lower(),
                "env": props[1],
                "when": props[3],
                "size": props[2],
                "jan": props[4],
                "feb": props[5],
                "mar": props[6],
                "apr": props[7],
                "may": props[8],
                "jun": props[9],
                "jul": props[10],
                "aug": props[11],
                "sep": props[12],
                "oct": props[13],
                "nov": props[14],
                "dec": props[15]
            }
    
    with open(fishPath, 'w') as f:
        json.dump(fishData, f)

def import_bugs():
    bugsPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\bug.json'
    itemPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\item.json'
    bugsData = None
    itemData = None
    itemCount = 0

    with open(bugsPath) as f:
        bugsData = json.load(f)
    with open(itemPath) as f:
        itemData = json.load(f)
    itemCount = len(itemData)

    with open('./tools/bugs_add.txt') as f:
        for line in f:
            props = line.rstrip().split('|')
            itemData[props[0].lower()] = {
                "id": itemCount,
                "name": props[0].lower(),
                "price": props[2],
                "type": "bug"
            }
            bugsData[props[0].lower()] = {
                "id": itemData[props[0].lower()]["id"],
                "name": props[0].lower(),
                "env": props[3],
                "when": props[4],
                "jan": props[5],
                "feb": props[6],
                "mar": props[7],
                "apr": props[8],
                "may": props[9],
                "jun": props[10],
                "jul": props[11],
                "aug": props[12],
                "sep": props[13],
                "oct": props[14],
                "nov": props[15],
                "dec": props[16]
            }
            itemCount += 1
    
    with open(itemPath, 'w') as f:
        json.dump(itemData, f)
    with open(bugsPath, 'w') as f:
        json.dump(bugsData, f)

def import_crafting():
    crafPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\crafting.json'
    itemPath = 'C:\\Users\\shrot\\Documents\\CodeProjects\\AC_Bot\\data\\item.json'
    crafData = None
    itemData = None
    itemCount = 0

    with open(crafPath) as f:
        crafData = json.load(f)
    with open(itemPath) as f:
        itemData = json.load(f)
    itemCount = len(itemData)

    with open('./tools/crafting_add.txt') as f:
        for line in f:
            props = line.rstrip().split('|')
            itemData[props[0].lower()] = {
                "id": itemCount,
                "name": props[0].lower(),
                "price": props[3],
                "type": "crafting"
            }
            crafData[props[0].lower()] = {
                "id": itemData[props[0].lower()]["id"],
                "name": props[0].lower(),
                "acquire":props[2]
            }
            itemCount += 1
    
    with open(itemPath, 'w') as f:
        json.dump(itemData, f)
    with open(crafPath, 'w') as f:
        json.dump(crafData, f)


import_crafting()
#import_items()
#import_fish()
#mport_bugs()