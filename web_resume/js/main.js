/* Configuaration for the game */ 
var config = {
    type: Phaser.AUTO,
    width: 960,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update,
        render:render
    }
};

/* Game objects declaration */
var platforms;
var player;
var coins;
var score = 0;
var scoreText;

/* game declaration */
var game = new Phaser.Game(config);

/* In this functio we preload the assets, now we can add this assets in the scene when we create one */
function preload () {

    this.load.image('background', 'images/background.png');
    this.load.image('ground', 'images/ground.png');
    this.load.spritesheet('coin', 'images/coin_animated.png', { frameWidth: 22, frameHeight: 22 });
    this.load.spritesheet('hero', 'images/hero.png',{ frameWidth: 36, frameHeight: 42 });

}

function create () {
    this.add.image(480, 300, 'background');
    
    /* 
       Creation of platform with gravity physics, I created a group for several 
       objects with the same physics caraterustics.
    */
    platforms = this.physics.add.staticGroup();
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    player = this.physics.add.sprite(150, 400, 'hero');

    player.setBounce(0.2);
    player.setCollideWorldBounds(true);

    /* Player animations */
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('hero', { start: 0, end: 2 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [ { key: 'hero', frame: 0 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('hero', { start: 0, end: 2 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'jump',
        frames: this.anims.generateFrameNumbers('hero', {start: 2, end: 3}),
        frameRate: 10,
        repeat: -1
    });

    /* Coin animation */ 
    this.anims.create({
        key: 'rotate',
        frames: this.anims.generateFrameNumbers('coin', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });

    /* Use cursors for moving the player */
    cursors = this.input.keyboard.createCursorKeys();

    /* In order to allow the played to collide with the platforms we can create a Collider object */
    this.physics.add.collider(player, platforms);

    /* Creation conis in the scene, possition random */ 
    coins = this.physics.add.group();
    for(var i = 0; i < 10; i++){
        createCoinSprite();
    }
    
   
    this.physics.add.collider(coins, platforms);
    this.physics.add.overlap(player, coins, collectCoin, null, this);

    /* Adding text score */
    scoreText = this.add.text(20, 20, 'score: 0', {fontsize: '32px', fill: '#000'}); 
}

function update() {
    if (cursors.left.isDown)
    {
        player.setVelocityX(-160);

        player.anims.play('left', true);
    }
    else if (cursors.right.isDown)
    {
        player.setVelocityX(160);

        player.anims.play('right', true);
    }
    else
    {
        player.setVelocityX(0);

        player.anims.play('turn');
    }

    if (cursors.up.isDown && player.body.touching.down)
    {
        player.setVelocityY(-330);

        player.anims.play('jump');
    }

    
}

function collectCoin (player, coin){
    coin.disableBody(true, true);

    score += 10;
    scoreText.setText('Score: ' + score);
}

function createCoinSprite() {
    let co = coins.create(Phaser.Math.Between(10, 950),100,'coin');
    co.anims.play('rotate', true);

}

function render() {

    // Sprite debug info

}

/* In Arcade Physics there are two types of physics bodies: Dynamic and Static. 
A dynamic body is one that can move around via forces such as velocity or acceleration. 
It can bounce and collide with other objects and that collision is influenced by the mass 
of the body and other elements.

In stark contrast, a Static Body simply has a position and a size. 
It isn't touched by gravity, you cannot set velocity on it and when something collides with it, 
it never moves. Static by name, static by nature. And perfect for the ground and platforms 
that we're going to let the player run around on.*/