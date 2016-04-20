# The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

def chooseStrategy():
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    # If you can summon a griffin-rider, return "griffin-rider"
    if self.gold > self.costOf("griffin-rider"):
        return "griffin-rider"
    # If there is a fangrider on your side of the mines, return "fight-back"
    elif enemy:
        for fangrider in self.findByType("fangrider"):
            if fangrider.pos < {"x": 38, "y": self.pos.y}:
                return "fight-back"        
    
    # Otherwise, return "collect-coins"
    else:
        return "collect-coins" 

def commandAttack():
    # Command your griffin riders to attack ogres.
    for griffin in self.findByType("griffin-rider"):
        if griffin:
            enemy = griffin.findNearest(griffin.findEnemies())
            if enemy:
                self.command(griffin, "attack", enemy)
    pass
    
def pickUpCoin():
    # Collect coins
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)
    pass
    
def heroAttack():
    # Your hero should attack fang riders that cross the minefield.
    enemies = self.findEnemies()
    
    for enemy in enemies:
        
        if self.isReady("power-up"):
            self.powerUp()
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)
    pass
    
loop:
    commandAttack()
    strategy = chooseStrategy()
    # Call a function, depending on what the current strategy is.
    if strategy == "griffin-rider":
        self.summon("griffin-rider")
    elif strategy == "fight-back":
        heroAttack()
    elif strategy == "collect-coins":
        pickUpCoin()
