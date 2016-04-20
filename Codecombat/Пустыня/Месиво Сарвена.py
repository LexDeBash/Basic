# Выживите в течении двух минут
# Если вы победите, уровень станет сложнее(и более прибыльным)
# Если вы проиграете, вы должны ждать день, чтобы повторно участвовать.
# Помните, каждая игра будет генерироваться случайно.

loop:
    enemies = self.findEnemies()
    for enemy in enemies:
        if enemy.type != "sand-yak":
            if self.isReady("power-up"):
                self.powerUp()
            elif self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)

