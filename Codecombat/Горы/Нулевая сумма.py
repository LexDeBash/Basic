# Одолей противника в течении двух минут.
loop:
    enemy = self.findNearest(self.findEnemies())
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)    
    # Твой герой может собирать монеты и призывать войска.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    
    # Она также командует твоими союзниками в битве.
    friends = self.findFriends()
    for soldier in friends:
        self.command(soldier, "attack", enemy)
    
    # Используй возможности персонажа, чтобы изменить исход сражения.
    
    
