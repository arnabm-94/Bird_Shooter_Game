# Bird_Shooter_Game
This is a simple game using Pygame, where the player controls a gun to shoot down birds while avoiding bombs, bricks, and rocks.

Initialization: Pygame is initialized, and screen dimensions, colors, and game variables are set up.

Loading Images: Images for the player, birds, bombs, bricks, rocks, and background are loaded and scaled to appropriate sizes.

Main Game Loop: The game runs within a main loop. Inside the loop:

Events are handled, primarily by quitting the game.
The left and right arrow keys control player movement.
Birds, bombs, bricks, and rocks are spawned randomly at specified rates.
Collisions between game elements are detected, and the game over condition is triggered accordingly.
Game elements are drawn on the screen.
Score and level are displayed on the screen.
Update Level Function: This function updates the game level based on the player's score.

Game Over Handling: When the game ends, a "game over" screen is displayed for 2 seconds before quitting the game.
