loop:
    enemies = self.findEnemies()
    for enemy in enemies:
        if enemy.type == "archer":
            if self.isReady("power-up"):
                self.powerUp()
            elif self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)
        enemy = self.findNearest(enemies)
        if enemy.type != "sand-yak":
            if self.isReady("power-up"):
                self.powerUp()
            elif self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)
