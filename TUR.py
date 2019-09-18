import random
class tur:

    def __init__(self,start,end,step,wall):
        self.start=start
        self.x=start[0]
        self.y=start[1]
        self.ex=end[0]
        self.ey=end[1]
        self.visited=[]
        self.stepSize=step
        self.wall=wall
        self.path=[]

    def setPath(self,pat):
        self.path=pat


    def goto(self,cor):
        self.x=cor[0]
        self.y=cor[1]



    def getRandomChild(self):

        ch=[]

        if self.y + self.stepSize <= 280:
            up=[self.x,self.y+20]
            if up not in self.wall+ self.visited:
                ch.append(up)
        if self.x + self.stepSize <= 280:
            right=[self.x+20,self.y]
            if right not in self.wall+ self.visited:
                ch.append(right)
        if self.y - self.stepSize >= -280:
            down=[self.x,self.y-20]
            if down not in self.wall+ self.visited:
                ch.append(down)
        if self.x - self.stepSize >= -280:
            left=[self.x-20,self.y]
            if left not in self.wall+ self.visited:
                ch.append(left)
        try:
            r=random.choice(ch)
        except:
            r=0
        return r


    def generatePath(self):
        self.path.append(self.start)
        queue=[]
        queue.append([self.x,self.y])

        while True:
            if self.x==self.ex and self.y==self.ey:
                break
            child=self.getRandomChild()
            if child==0:
                while child==0:
                    p=queue.pop()
                    self.goto(p)
                    child=self.getRandomChild()
            else:
                self.visited.append(child)
                self.path.append(child)
                queue.append(child)
                self.goto(child)



    def fitnessFunction(self):
        return len(self.path)
