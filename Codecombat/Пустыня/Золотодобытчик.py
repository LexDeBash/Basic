# Чтобы быстро собрать много золота, просто собирай золотые монеты.

loop:
    coins = self.findItems()
    coinIndex = 0
    
    # Заключи код в цикл, проверяющий все монеты.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex +=1
        # Стоимость золотой монеты равна 3.
        if coin.value == 3:
            # Собирайте только золотые монеты.
            self.moveXY(coin.pos.x, coin.pos.y)
            coinIndex +=1
            pass
            

    
