import turtle
import os
import math
import random
# set up the screen
win=turtle.Screen()
win.bgcolor("black")
win.title("space invadors game")
win.bgpic("BG1.gif")
# creating borders
border=turtle.Turtle()
border.shape("circle")
border.color("red")

border.speed(0)
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()
# set the score to 0
score=0
# draw the score
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.setposition(-290,280)
# scorestring="SCORE : {}".format(score)
# score.write(scorestring,align="center", font=("candara",24,"bold"))
score.write("SCORE : {} ".format(score),False, align="center", font=("candara", 24, "bold"))

score.hideturtle()
# register the shape
turtle.register_shape("player1.gif")
# create the player turtle
player=turtle.Turtle()
player.color("pink")
player.shape("player1.gif")
player.penup()
player.setposition(0,-250)
player.setheading(90)
playerspeed=15



# choose a numebr of enemies
number_of_enemies=5
# create an empty list of enemies
enemies=[]
# add enemies to the list
for i in range(number_of_enemies):
#     create the enemy
    turtle.register_shape("enemy4 edited.gif")
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy4 edited.gif")
    enemy.penup()
    enemy.setposition(-250,250)
    enemy.setheading(270)
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed=8
# creating bullet turtle
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=20
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)
def move_right():
    z=player.xcor()
    z+=playerspeed
    if z>280:
        z=280
    player.setx(z)

# creating a function fro firing the bullet
def fire_bullet():
#     declaring bullet state as a global scope of variable
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        # positioning the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# creating the function for detecting the c0ollision between 2 objects/ the enemy and the bullet
def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<30:
        return True
    else:
        return False



# create keyboard bindings

turtle.onkey(move_left, "Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
turtle.listen()
while True:
    for enemy in enemies:

    # move the enemy
        x=enemy.xcor()
    # x=-250
        x+=enemyspeed
    # x=x+enemyspeed
    # x=-250+2
    # x=-248
        enemy.setx(x)
    # to bring the enemy back
        if enemy.xcor()>280:
 # when the enemys xcor is greater than 280 then the enemys speed should be multiplied by -1
            for e in enemies:
                y=e.ycor()
                # y=250
                y-=40
                # y=y-40
                # y=250-40
                # y=210
                e.sety(y)
            enemyspeed*=-1

    #     enemyspeed=enemyspeed*-1
    # enemyspeed=2*-1
    # enemyspeed=-2
        if enemy.xcor()<-280:
           for e in enemies:

                y=e.ycor()
                y-=40
                e.sety(y)
           enemyspeed*=-1

    #     move the bullet
        y=bullet.ycor()
        y+=bulletspeed
    # y=y+bulletspeed
    # y=-250+20=-230 keeps going up and up till the end

        bullet.sety(y)
    # checking to see if the bullet has gone out of the canvas
        if bullet.ycor()>275:
            bullet.hideturtle()
            bulletstate="ready"
    # move the bullet
    # if bulletstate=="fire":
    #     y=bullet.ycor()
    #     y=y+bulletspeed
    #     bullet.sety(y)

    # check fro the collision in the enemy and the bullet
        if isCollision(bullet,enemy):
        # reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
        # reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
    #         update the score
    #         score+=10
            score=score+10
            score.write("SCORE : {}".format(score),align="center",font=("candara",24,"bold"))

    win.update()

