# ANGM2305_FinalProject
Final project for ANGM2305

## Demo
Video: <https://youtu.be/5yGXmMvzPWw>


## Git Repo
Github Link: <https://github.com/carterburkett/ANGM2305_FinalProject/tree/main>


## Description
This project is a fully play version of pong. The AI increase with difficulty based off of the players score. And the collision algorithm checks the positions of the participating paddles, the ball’s current position, and the approximate next position of the ball. This provides two layers of detection.

### Collision
Layer 1 is between the ball’s next position, and the current position of the paddle. This should handle most collision cases as it is searching for a collision before it’s happened. If the ball collides, its velocity is reversed. The second layer is the collision between the actual position of the ball, and the position of the paddle. In the event the paddle moves into the ball, or the ball bounces off the wall in a way that the first layer of protection does not detect or expect, the program can still catch the collision and send the ball back to the other player.


###Challenges
Getting the multiple classes to work together and talk to eachother in a way that was not redundant was a challenge in python. I am used to working with structs and lists in C++/C#. While Python's libraries and dictionaries are very similar to those two tools, when starting to build the game I found that they were almost too heavy for a game like Pong. It added a layer of complexity that only hindered the code and the game. So i made the decision to not use them and approach the game in a way that I thought was more becoming of a Python program; Python's strengths lie in its abililty to stay simple.


### Future Improvements
In the future, I would like to improve on quality of life aspects of the game. The game would be heavily improved with more visual feedback and game music. Additionally, the game would benefit from things such as powerups, and different game modes. 


## Dependencies
This game is reliant upon pygame. Pygame was primarily used as a convenient way to create Rects, and provide a base to a collision algorithm. It also handles the game’s display, text, etc. 

Pygame: <https://www.pygame.org/>

Python Random: <https://www.w3schools.com/python/module_random.asp>

##References:
"Very Simple Pong Game (Pygame)": <https://www.pygame.org/project-Very+simple+Pong+game-816-.html>

"Pong Tutorial using Pygame" : <https://www.101computing.net/pong-tutorial-using-pygame-getting-started/>

Previous Experince with Pong: <https://www.youtube.com/watch?v=qWk3NywldIM&list=PLDVE0HI6K5Y4pnCYBdwN5fWwj7ZvufYhL&index=5>



