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

/* game declaration */
var game = new Phaser.Game(config);

/* In this functio we preload the assets, now we can add this assets in the scene when we create one */
function preload () {

    //this.load.crossOrigin = 'Anonymous';
    this.load.image('background', 'images/background.png');
    this.load.image('ground', 'images/ground.png');

}

var platforms;

function create () {
    this.add.image(480, 300, 'background');

    /* 
       Creation of platform with gravity physics, I created a group for several 
       objects with the same physics caraterustics.
    */
    platforms = this.physics.add.staticGroup();
    platforms.create(400, 558, 'ground').setScale(2).refreshBody();

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