# Соберите монеты, чтобы вызвать солдат и атаковать ими врагов.

loop:
    # Переход к ближайшей монете.
    # Используйте 'move' вместо 'moveXY', чтобы командовать постоянно.
    #self.say("Мне нужны монеты!")
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)

    # Если у вас достаточно монет для солдата, вызвать одного.
    if self.gold > self.costOf("soldier"):
        #self.say("Я должен здесь что-то вызвать!")
        self.summon("soldier")

    enemy = self.findNearest(self.findEnemies())
    if enemy:
        # Цикл по всем вашим солдатам и приказ им об атаке.
        soldiers = self.findFriends()
        soldierIndex = 0
        while soldierIndex < len(soldiers):
            soldier = soldiers[soldierIndex]
            # Используйте команду 'attack', чтобы заставить ваших солдат атаковать.
            self.command(soldier, "attack", enemy)
            soldierIndex +=1

        
