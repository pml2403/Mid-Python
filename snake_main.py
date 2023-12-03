from snake_assets.snake_settings import *
import time
import random

#Main game
while True:
    scr.update()
    #Check game over
    #Crash into wall
    if my_snake.xcor() > GAME_WIDTH / 2 - SPACE_SIZE or my_snake.xcor() < -(GAME_WIDTH / 2 - SPACE_SIZE) or my_snake.ycor() > GAME_HEIGHT / 2 - SPACE_SIZE or my_snake.ycor() < -(GAME_HEIGHT / 2 - SPACE_SIZE):
        game_over_sound()
        time.sleep(1)
        my_snake.goto(0,0)
        my_snake.direction = "stop"
        for block in blocks:
            block.goto(GAME_WIDTH + 100, GAME_HEIGHT + 100)
        #Reset game
        blocks.clear()
        score = 0
        delay = 0.1
        score_line.clear()
        score_line.write(f'Score: {score}  High Score: {high_score}', align = "center", font = ("Arial", 25, "normal")) 
    #Hit its tail
    for block in blocks:
        if block.distance(my_snake) < 20:
            game_over_sound()
            time.sleep(1)
            my_snake.goto(0,0)
            my_snake.direction = "stop"
            for block in blocks:
                block.goto(GAME_WIDTH + 100, GAME_HEIGHT + 100)
            #Reset game
            blocks.clear()
            score = 0
            delay = 0.1
            score_line.clear()
            score_line.write(f'Score: {score}  High Score: {high_score}', align = "center", font = ("Arial", 25, "normal")) 

    #Food
    if my_snake.distance(my_food) < SPACE_SIZE:
        my_food.goto(random.randint(-(GAME_WIDTH / 2 - SPACE_SIZE), GAME_WIDTH / 2 - SPACE_SIZE), random.randint(-(GAME_WIDTH / 2 - SPACE_SIZE), GAME_WIDTH / 2 - SPACE_SIZE))
        #Add block to snake
        new_block = turtle.Turtle()
        new_block.speed(0)
        new_block.shape(SNAKE_SHAPE)
        new_block.color("light blue")
        new_block.penup()
        blocks.append(new_block)
        play_sound()

        #Increase speed
        delay -= 0.001

        #Increase score
        score += 10

        if score > high_score:
            high_score = score
        score_line.clear()
        score_line.write(f'Score: {score}  High Score: {high_score}', align = "center", font = ("Arial", 25, "normal")) 

    #increase snake's length
    for index in range(len(blocks)-1, 0, -1):
        blocks[index].goto(blocks[index-1].xcor(), blocks[index-1].ycor())

    #Link blocks to snake
    if len(blocks) > 0:
        blocks[0].goto(my_snake.xcor(), my_snake.ycor())

    #Run game
    snake_game.move()    
    time.sleep(delay)

scr.mainloop()
