# Прикажите вашим войскам двигаться на восток и атаковать любых огров которых они увидят.
# Используйте for циклы и findFriends.
# Вы можете использовать метод findNearestEnemy() на Ваших солдатах, для того, чтобы находить ближайшего к ним, а не к себе, противника.
loop:
    friends = self.findFriends()
    for friend in friends:
        enemy = friend.findNearestEnemy()
        if enemy:
            self.command(friend, "attack", enemy)
        else:
            self.command(friend, "move", ({"x": 30, "y":friend.pos.y}))
            if friend.type == "archer":
                archer = friend
                if archer.health < archer.maxHealth/1.3:
                    self.command(friend, "move", ({"x": friend.pos.x-4, "y":friend.pos.y}))
                else:
                    self.command(friend, "move", ({"x": friend.pos.x+1, "y":friend.pos.y}))
                
            else if friend.type == "soldier":
                time = self.now()
                if time > 4.5:
                    self.command(friend, "move", ({"x": friend.pos.x+0.5, "y":friend.pos.y}))

                
                
                

