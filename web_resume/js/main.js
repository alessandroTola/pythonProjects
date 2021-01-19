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
        create: create
    }
};

/* Game objects declaration */
var platforms;
var player;

/* game declaration */
var game = new Phaser.Game(config);

/* In this functio we preload the assets, now we can add this assets in the scene when we create one */
function preload () {

    //this.load.crossOrigin = 'Anonymous';
    this.load.image('background', 'images/background.png');
    this.load.image('ground', 'images/ground.png');
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

    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('hero', { start: 0, end: 2 }),
        frameRate: 10,
        repeat: -1
    });

    /*this.anims.create({
        key: 'turn',
        frames: [ { key: 'hero', frame: 4 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('hero', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });*/

    /* In order to allow the played to collide with the platforms we can create a Collider object */
    this.physics.add.collider(player, platforms);
}

function update() {

}


/* In Arcade Physics there are two types of physics bodies: Dynamic and Static. 
A dynamic body is one that can move around via forces such as velocity or acceleration. 
It can bounce and collide with other objects and that collision is influenced by the mass 
of the body and other elements.

In stark contrast, a Static Body simply has a position and a size. 
It isn't touched by gravity, you cannot set velocity on it and when something collides with it, 
it never moves. Static by name, static by nature. And perfect for the ground and platforms 
that we're going to let the player run around on.*/