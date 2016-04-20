defendPoints = [{"x": 41, "y": 46},{"x": 40, "y": 25}]
summonTypes = ["soldier","archer", "soldier", "archer"]


def goldFarm():
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)
        


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold >= self.costOf(type):
        self.summon(type)
  
        
def commandTroops():
    friends = self.findFriends()
    for friendIndex, friend in enumerate(friends):
        if friend.type == "soldier" or friend.type == "archer":
            defPoints = defendPoints[friendIndex % len(defendPoints)]
            self.command(friend, "defend", defPoints)


loop:
    goldFarm()
    summonTroops()
    commandTroops()
