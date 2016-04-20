loop {
    var enemies = this.findEnemies();
    for (i = 0; i < enemies.length; i++){
        var enemy = enemies[i];
        if (enemy.type == "archer") {
            if (this.isReady("power-up")){
                this.powerUp();
            }
            else if (this.isReady("bash")){
                this.bash(enemy);
            }
            else {
                this.attack(enemy);
            }
        }
        enemy = this.findNearest(enemies);
        if (enemy.type != "sand-yak") {
            if (this.isReady("power-up")){
                this.powerUp();
            }
            else if (this.isReady("bash")){
                this.bash(enemy);
            }
            else {
                this.attack(enemy);
            }
        }
    }
}
