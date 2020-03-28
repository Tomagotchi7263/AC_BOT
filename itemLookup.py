def ItemLookup(itemName):
    import json
    itemData = None
    fishData = None
    bugsData = None
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    outString = ""

    with open('./data/item.json') as f:
        itemData = json.load(f)

    try:
        target = itemData[itemName]
        outString += "Name: %s \nPrice: %s \nType: %s" % (target["name"], target["price"], target["type"])
        if target["type"] == "fish":
            with open('./data/fish.json') as f:
                fishData = json.load(f)
            fishTarget = fishData[itemName]
            outString += "\nEnvironment: %s \nWhen: %s \nSize: %s \nAvailable: " % (fishTarget["env"], fishTarget["when"], fishTarget["size"])
            availString = ""
            availCount = 0
            for month in months:
                if fishTarget[month] == 1:
                    availString += month + ", "
                    availCount += 1
            if availCount == 12:
                availString = "All Year"
            outString += availString
    except:
        outString = "Something went wrong no results for %s" % itemName
    return outString
