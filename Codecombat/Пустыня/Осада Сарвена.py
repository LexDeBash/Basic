# Defend your towers in this replayable challenge level!
# Step on an X if you have 20 gold to build a soldier.
loop:
    coin = self.findNearest(self.findItems())
    time = self.now()
    if coin and time < 20:
        self.moveXY(coin.pos.x, coin.pos.y)
    else:
        self.moveXY(84, 78)
        self.moveXY(84, 51)
        self.moveXY(84, 22)
        break

loop:
    enemy = self.findNearest(self.findEnemies())
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    elif enemy:
        if self.isReady("power-up"):
            self.powerUp()
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)

