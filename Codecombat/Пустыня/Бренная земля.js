// Используй свои умнейшние программные трюки, чтобы победить оппонента!
loop {
    var enemies = this.findEnemies();
    for (var i = 0; i < enemies.length; i++){
        var enemy = enemies[i];
        if (enemy.type == "sand-yak") {
            continue;
        }
        if (enemy.type == "archer") {
            if (this.isReady("power-up")) {
                this.powerUp();
            }
            else if (this.isReady("bash")) {
                this.bash(enemy);
            }
            else {
                this.attack(enemy);
            }
        }
        else {
            if (this.isReady("power-up")) {
                this.powerUp();
            }
            else if (this.isReady("bash")) {
                this.bash(enemy);
            }
            else {
                this.attack(enemy);
            }            
        }
    }
}
