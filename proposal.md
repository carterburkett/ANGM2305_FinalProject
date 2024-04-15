# ANGM 2305 Final Project: Pong in Python

## Repository Link
<https://github.com/carterburkett/ANGM2305_FinalProject.git>

## Description
A simple implementation of Pong in Python. Players will control one paddle, and play against a simple AI. They will either win or lose based off of their score.

## Features
-Feature 1:
  -Paddle is controllable through keyboard input and will be tied to a set framerate.
-Feature 2:
  -There will be a basic AI in the game. It will scale in difficulty according to the player's skill.
-Feature 3:
  -The scores will be displayed in game so the player can see them.

## Challenges
-Creating an AI that responds appropriately in both difficulty and timing.
  -The AI will likley "chase" the ball at a given speed(s), but only when the ball is moving towards the paddle
-Creating a collision Algorithm
  -A basic AABB collision alogrithm will have to be written. However, this can be deceptfully difficult in a language i have little familiarity with. 
-Creating an acceleration/Deacceleartion algorithm.
  -This is difficult because the ball should interact with certain behaviors depending on the direction of the ball and paddle, as well as where it hits on the paddle.

## Outcomes
Ideal Outcome:
- A functional game of pong where the ball does not clip inside of, or through the paddles

Minimal Viable Outcome:
-A functional game of pong where the AI is slighlty easier or more difficult than it should be, and where there are still some sporatic cases of clipping during ball collisions

# Milestones
-Week 1:
  -A basic drawn "board"
  -A controllable paddle
  -An imperfect AI paddle
  -A ball that moves and, at the very least, collides with the boundaries of the board

-Week 2:
  -Ball collides with paddles
  -Ball acts appropriately with collision cases
  -Ball has variable speeds
  -Scoring implemented and working

-Final Week:
  -Game is mostly functional at this point
  -Primarily debugging and fine tuning errors/bugs that arise.
  -Cleaning code
