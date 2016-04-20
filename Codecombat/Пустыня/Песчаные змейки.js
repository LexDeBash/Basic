//Песчаные змеи
//Самая короткая дистанция до предмета
loop;
{
    var coins = this.findItems();
    var coinIndex = 0;
    var nearest = null;
    var nearestDistance = 9999;
    while (coinIndex < coins.length) {
        var coin = coins[coinIndex];
        coinIndex++;
        var distance = this.distanceTo(coin);
        if (distance < nearestDistance) {
            nearestDistance = distance;
            nearest = coin;
        }
    }
    this.moveXY(nearest.pos.x, nearest.pos.y);
}
