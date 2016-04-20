# The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

def chooseStrategy():
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    
    # If you can summon a griffin-rider, return "griffin-rider"
    
    if self.gold > self.costOf("griffin-rider"):
        return "griffin-rider"
    
    # If there is a fangrider on your side of the mines, return "fight-back"
    
    elif enemy and enemy.pos.x < 38:
        return "fight-back"        
    
    # Otherwise, return "collect-coins"
    
    else:
        return "collect-coins" 

def commandAttack():
    # Command your griffin riders to attack ogres.
    for griffin in self.findByType("griffin-rider"):
        if griffin:
            enemies = griffin.findEnemies()
            for enemy in enemies:
                if enemy.type != "fangrider":
                    self.command(griffin, "attack", enemy)
    pass
    

def witch():
    # Command your griffin riders to attack witch.
    for griffin in self.findByType("griffin-rider"):
        if griffin:
            enemies = griffin.findEnemies()
            for witch in self.findByType("witch"):
                while witch.helth > 0:
                    self.command(griffin, "attack", witch)
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
        enemy = self.findNearest(enemies)
        if enemy and enemy.type == "fangrider":
            
            if self.isReady("power-up"):
                self.powerUp()
            elif self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)
    pass
    
    
loop:
    enemies = self.findEnemies()
    for enemy in enemies:
        if enemy.type == "witch":
            witch()
        else:
            commandAttack()
    strategy = chooseStrategy()
    # Call a function, depending on what the current strategy is.
    if strategy == "collect-coins":
        pickUpCoin()
    elif strategy == "griffin-rider":
        self.summon("griffin-rider")
    else if strategy == "fight-back":
        heroAttack()
