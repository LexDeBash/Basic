# Ogres are trying to kill your reindeer!
# Keep your archers back while summoning soldiers to attack.

def pickUpCoin():
    # Collect coins.
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)


def summonTroops():
    # Summon soldiers if you have the gold.
    while self.gold > self.costOf("soldier"):
        self.summon("soldier")
        
        

# This function has an argument named soldier.
# Arguments are like variables.
# The value of an argument is determined when the function is called.
def commandSoldier(soldier):
    # Soldiers should attack enemies.
    enemy = friend.findNearestEnemy()
    if enemy:
        if friend.health < friend.maxHealth / 1.5:
            self.command(friend, "move", ({"x": 27, "y": friend.pos.y}))
        else:
            self.command(friend, "attack", enemy)
    pass


# Write a commandArcher function to tell your archers what to do!
# It should take one argument that will represent the archer passed to the function when it's called.
# Archers should only attack enemies who are closer than 25 meters, otherwise, stay still.
def commandArcher(archer):
    # Soldiers should attack enemies.
    enemy = friend.findNearestEnemy()
    if enemy:
        distance = friend.distanceTo(enemy)
        if distance >= 25:
            self.command(friend, "move", friend.pos)
        else:
            self.command(friend, "attack", enemy)
    pass

loop:
    pickUpCoin()
    summonTroops()
    friends = self.findFriends()
    for friend in friends:
        if friend.type == "soldier":
            # This friend will be assigned to the variable soldier in commandSoldier
            commandSoldier(friend)
        elif friend.type == "archer":
            commandArcher(friend)
            pass

