/* Configuaration for the game */ 
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create
    }
};

/* game declaration */
var game = new Phaser.Game(config);

/* In this functio we preload the assets, now we can add this assets in the scene when we create one */
function preload ()
{

    //this.load.crossOrigin = 'Anonymous';
    this.load.image('background', 'images/background.png');
}

function create ()
{
    this.add.image(400, 300, 'background');
}

