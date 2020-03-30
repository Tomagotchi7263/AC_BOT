class StalkMarket:
    def __init__(self):
        import json
        from datetime import date, timedelta, datetime
        self.masterData = None
        self.date = str(date.today())                           # Today's date YYYY-MM-DD
        self.yesterday = str(date.today() - timedelta(days=1))  # Yesterday's date YYYY-MM-DD
        self.day = datetime.today().strftime('%A')              # Day of the week
        with open('./data/stalk.json') as f:
            self.masterData = json.load(f)
        self.users = self.masterData["users"]
        self.userData = None
        with open('./data/users.json') as f:
            self.userData = json.load(f)
        try:
            self.todayData = self.masterData["data"][self.date]
            print('loaded todays data')
        except:
            self.masterData['data'][self.date] = {}
            for user in self.users:
                try:
                    self.masterData['data'][self.date][user] = {
                        "owns": 0 if self.day == "Sunday" else self.masterData['data'][self.yesterday][user]["owns"],   # Grabs yesterday's turnip count unless it is Sunday
                        "price": 0
                    }
                except KeyError:
                    # this except is here for new users that didnt have an entry the day before
                    self.masterData['data'][self.date][user] = {
                        "owns": 0,
                        "price": 0
                    }

            with open('./data/stalk.json', 'w') as f:
                json.dump(self.masterData, f)
            self.todayData = self.masterData['data'][self.date]
            print('created and loaded todays data')

    def Process(self, message, client):
        returnString = ""
        helpMsg = "\nType `!turnip help` for help!"
        commands = message.content.split(' ')
        print(commands)
        if len(commands) <= 3 and len(commands) > 1:
            if commands[1].lower() == "reg":
                if len(commands) > 3:
                    returnString = "You supplied too many arguments! %s" % helpMsg
                elif len(commands) < 3:
                    returnString = "You did not supply a price! %s" % helpMsg
                else:
                    try:
                        price = int(commands[2])
                        if str(message.author) not in self.users:
                            t = self.WriteData(str(message.author), "user")
                        returnString = self.WriteData((str(message.author), price), "price")
                    except ValueError:
                        returnString = "%s is not a valid number! %s" %(commands[2], helpMsg)
            elif commands[1].lower() == "buy":
                if len(commands) > 3:
                    returnString = "You supplied too many arguments! %s" % helpMsg
                elif len(commands) < 3:
                    returnString = "You did not supply a number! %s" % helpMsg
                else:
                    try:
                        num = int(commands[2])
                        if str(message.author) not in self.users:
                            t = self.WriteData(str(message.author), "user")
                        returnString = self.WriteData((str(message.author), num), "buy")
                    except ValueError:
                        returnString = "%s is not a valid number! %s" %(commands[2], helpMsg)
            elif commands[1].lower() == "help":
                returnString = "Here is a list of commands relating to the stalk market!\n"
                returnString += "`!turnip reg [number]`\n> This registers the current price that your island is offering for turnips!\n> Please remember that your turnip prices change at 12PM!\n"
                returnString += "`!turnip buy [number]`\n> This helps you keep track of how many turnips you've bought.\n> In the future, the prices command will help calculate your payout.\n"
                returnString += "`!turnip me`\n> This displays information related to your turnip market.\n"
                returnString += "`!turnip prices`\n> This displays turnip prices across everyone's islands.\n"
                returnString += "`!turnip help`\n> This displays this menu."
            elif commands[1].lower() == "me":
                owned = str(self.masterData["data"][self.date][str(message.author)]["owns"])
                price = str(self.masterData["data"][self.date][str(message.author)]["price"])
                if self.day == "Sunday":
                    returnString = "%s, you own %s turnips!" % (str(message.author.display_name), owned)
                else:
                    returnString = str(message.author.display_name) + ","
                    if owned == "0":
                        returnString += "\nYou didn't buy any turnips this week!"
                    else:
                        returnString += "\nYou own %s turnips!" % owned
                    if price == "0":
                        returnString += "\nYou haven't registered your island's turnip price today!"
                    else:
                        returnString += "\nYour island is buying turnips for %s bells today!" % price
            elif commands[1].lower() == "prices":
                for user in self.users:
                    price = str(self.masterData["data"][self.date][user]["price"])
                    userObj = client.get_user(self.userData[user]["id"])
                    if self.day == "Sunday":
                        returnString = "The stalk market is closed today! Check back tomorrow!"
                    else:
                        if price != "0":
                            returnString += "%s: %s bells per turnip.\n> Your payout would be %i bells!" % (userObj.display_name, price, (int(self.masterData["data"][self.date][str(message.author)]["owns"]) * int(price)))
                        else:
                            returnString += "%s has not registered their turnip price today!\n" % userObj.display_name
            else:
                returnString = "%s is not a recognized command! %s" % (commands[1], helpMsg)
        elif len(commands) == 1:
            returnString = "You didn't supply any arguments! %s" % helpMsg
        else:
            returnString = "You supplied too many arguments! %s" % helpMsg 
        #return(message.author)
        return returnString
    
    def WriteData(self, data, dataType):
        import json
        returnString = ""
        if dataType == "user":
            self.masterData["users"].append(data)
        elif dataType == "price":
            if self.day == "Sunday":
                returnString = "You cannot sell turnips on Sundays!"
            else:
                self.masterData["data"][self.date][data[0]]["price"] = data[1]
                returnString = "You set your island's turnip price to %s!" % str(self.masterData["data"][self.date][data[0]]["price"])
            print('TODO PRICE')
        elif dataType == "buy":
            if self.day == "Sunday":
                self.masterData["data"][self.date][data[0]]["owns"] += data[1]
                returnString = "You bought %s turnips! You now own %s turnips!" % (str(data[1]), str(self.masterData["data"][self.date][data[0]]["owns"]))
            else:
                returnString = "Sorry! But you can only buy turnips on Sunday!\n Don't tell me you're time traveling!"
        
        with open('./data/stalk.json', 'w') as f:
            json.dump(self.masterData, f)

        return returnString
            