from player_std import *
from mazes import *
import GA




# no need to change anything in this file.
stepSize = 20

# set up the maze:
level = levels[3]  # levels are from 1 to 8. See mazes.py filepopulation.append([f1,t])
wall, start, end = setUpMaze(level, stepSize)
count=0
nrGen=int(input('Enter numbers of generations you want to train'))
nrPop=int(input('Enter number of population you want to train'))

GA.generatePopulation(nrPop,start,end,stepSize,wall)
GA.sort()
print(GA.population[0][0])
c=0

while count<nrGen:

    parents=GA.selectParents()
    re=GA.crossOver(parents,start,end,stepSize,wall)
    if c==100:
        GA.mutation(nrPop,start,end,stepSize,wall)
        c=0
    c+=1
    if re==0:
        while re==0:
            parents=GA.selectParents()
            re=GA.crossOver(parents,start,end,stepSize,wall)
    count+=1
    GA.sort()
print('Done. Press q')
bestFitness, obj=GA.ret()
shpath=obj.path

agent = Player(start[0], start[1], 100)
agent.shape('square')
agent.color('green')

agent.penup()

target = Player(end[0], end[1], 100)
target.shape('square')
target.color('yellow')

#----Pause the animation until pressed q
starts = False
def play():
    global starts
    starts = True
# Set keyboard bindings
turtle.penup()
turtle.hideturtle()
turtle.listen()
turtle.onkey(play ,'q')
s = time.time()
while starts != True:
    turtle.setposition(-200,280)
    turtle.write("Press q to start ", align='center', font=("Arial",14,'bold'))
#---------------------------------------




# prints time and number of steps on the screen
dur = time.time() - s
turtle.hideturtle()
turtle.goto(0,-270)
turtle.write("It took %.2f seconds" % dur, align='center', font=("Arial",12,'bold'))
turtle.penup()
turtle.goto(0,-290)
turtle.write("The length of the path is {} steps".format(str(len(shpath))), align='center', font=("Arial",12,'bold'))

# draws the path that returned by Algorithms.---
finisher = Player(start[0], start[1], 1 )
finisher.pendown()
finisher.shape('classic')
finisher.width(4)
finisher.pencolor('green')
for i in shpath:
    finisher.goto(i)
#------------------------------------------

turtle.done()
