def ItemLookup(itemName):
    import json
    itemData = None
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    outString = ""

    with open('./data/item.json') as f:
        itemData = json.load(f)

    try:
        target = itemData[itemName]
        outString += "Name: %s \nPrice: %s \nType: %s" % (target["name"], target["price"], target["type"])
        if target["type"] == "fish" or target["type"] == "bug":
            with open('./data/' + target["type"] + '.json') as f:
                subData = json.load(f)
            subTarget = subData[itemName]
            if target["type"] == "fish": outString += "\nEnvironment: %s \nWhen: %s \nSize: %s \nAvailable: " % (subTarget["env"], subTarget["when"], subTarget["size"])
            else: outString += "\nEnvironment: %s \nWhen: %s \nAvailable: " % (subTarget["env"], subTarget["when"])
            availString = ""
            availCount = 0
            for month in months:
                if subTarget[month] == "1":
                    availString += month + ", "
                    availCount += 1
            if availCount == 12:
                availString = "All Year"
            outString += availString
        if target["type"] == "crafting":
            with open('./data/' + target["type"] + '.json') as f:
                subData = json.load(f)
            subTarget = subData[itemName]
            outString += "\nMethod: %s" % subTarget["acquire"]
    except:
        outString = "Something went wrong no results for %s" % itemName
    return outString
