// "findEnemies" возвращает список всех ваших врагов.
// Атаковать только шаманов. Не нападайте на яков!
var enemies = this.findEnemies();
var enemyIndex = 0;
// Заключите весь код в цикл 'While', чтобы код учитывал весь список врагов.
// While the enemyIndex is less than the length of enemies
while (enemyIndex < 6) {
    var enemy = enemies[enemyIndex];
    if (enemy.type == 'shaman') {
        this.moveXY(enemy.pos.x, enemy.pos.y);
        this.say("Wake up");
        enemyIndex += 1;
        while (enemy.health > 0) {
            this.attack(enemy);
        }
    }    // Remember to increment enemyIndex
    else {
        enemyIndex += 1;
    }
}
