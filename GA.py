import TUR
import random



population=[]

def ret():
    return population[0]

def sort ():
    population.sort(key=lambda r:r[0])

def generatePopulation(nrPop,start,end,step,wall):

    for i in range(nrPop):
        t1=TUR.tur(start,end,step,wall)
        t1.generatePath()
        fit=t1.fitnessFunction()
        population.append([fit,t1])


def selectParents():
    p=[]
    parents=[]

    for i in range(9):
        p.append(population[i])
    for i in range(2):
        r=random.uniform(0,1)
        if r<=0.3:
            parents.append(p[0])
            p.pop(0)
        elif r>0.3 and r<=0.5:
            parents.append(p[1])
            p.pop(1)
        elif r>0.5 and r<=0.65:
            parents.append(p[2])
            p.pop(2)
        elif r>0.65 and r<=0.75:
            parents.append(p[3])
            p.pop(3)
        elif r>0.75 and r<=0.85:
            parents.append(p[4])
            p.pop(4)
        elif r>0.85 and r<=0.9:
            parents.append(p[5])
            p.pop(5)
        elif r>0.9 and r<=0.95:
            parents.append(p[6])
            p.pop(6)
        elif r>0.95 :
            parents.append(p[7])
            p.pop(7)





    return parents

def mutation(nr,start,end,step,wall):
    r=random.randint(3,nr-1)
    population.pop(r)
    t=TUR.tur(start,end,step,wall)
    t.generatePath()
    fit=t.fitnessFunction()
    population.append([fit,t])



def crossOver(parents,start,end,step,wall):
    list=[]
    c1,p1=parents[0]
    c2,p2=parents[1]
    path1=p1.path
    path2=p2.path
    # s1=int(round(c1/3))
    # e1=s1*2
    # s2=int(round(c2/3))
    # e2=s2*2
    # slice1=path1[s1:e1]
    # slice2=path2[s2:e2]

    for i in path1:##slice1
        if i in path2:##slice2
            list.append(i)
    try:
        r=random.choice(list)
    except(IndexError):
        return 0
    index1=path1.index(r)
    index2=path2.index(r)

    cpath1=path1[:index1+1]+path2[index2:]
    cpath2=path2[:index2+1]+path1[index1:]

    t=TUR.tur(start,end,step,wall)
    t.setPath(cpath1)
    f1=t.fitnessFunction()
    population.pop()


    t2=TUR.tur(start,end,step,wall)
    t2.setPath(cpath2)
    f2=t2.fitnessFunction()
    population.pop()

    population.append([f1,t])
    population.append([f2,t2])

    return 1
