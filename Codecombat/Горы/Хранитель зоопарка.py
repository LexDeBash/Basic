# Защити клетку.
# Поставь солдата на каждый Х.
points = []
points[0] = {"x": 33, "y": 42}
points[1] = {"x": 47, "y": 42}
points[2] = {"x": 33, "y": 26}
points[3] = {"x": 47, "y": 26}

# Собери 80 золота.
while self.gold < 80:
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)
        pass
# Призови четырех солдат.
for i in range(4):
    self.summon("soldier")
    
# Отправь своих солдат на позиции.
loop:
    friends = self.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            # Прикажи войскам атаковать.
            self.command(friend, "attack", enemy)
            pass
            
        else:
            # Прикажи войскам двигаться на точку.
            self.command(friend, "move", point)
            pass
            
            
