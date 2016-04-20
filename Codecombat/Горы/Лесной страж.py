loop:
    # Собирай золото.
    coin = self.findNearest(self.findItems())
    if coin:
        self.move(coin.pos)
    # Если золота достаточно, призывай солдат.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    # При помощи for-цикла отдавай приказы каждому солдату.
    # For-циклы состоят из 2 частей: "for X in Y"
    # Y - массив в котором выполняется цикл.
    # Цикл выполняется один раз для каждого элемента Y, а X - определяет текущий элемент.
    for friend in self.findFriends():
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            # Если видишь врага прикажи атаковать.
            # Если нет, прикажи следовать в правую часть карты.
            if enemy:
                self.command(friend, "attack", enemy)
            else:
                self.command(friend, "move", ({"x": 78, "y": 48}))
                
            
            
