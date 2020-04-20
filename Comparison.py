import random
import math
import csv
import matplotlib.pyplot as plt

def gamePARS(ra,rb):
    p=ra/(ra+rb)
    pointsA=0
    pointsB=0
    rally=0
    while True:
        r = random.random() 
        if r<p:
            pointsA=pointsA+1
        else:
            pointsB=pointsB+1
        rally+=1
        if (math.fabs(pointsA-pointsB)>=2) and (pointsA>=11 or pointsB>=11) :
            return pointsA,pointsB,rally

def gameEnglish(ra,rb):
    p=ra/(ra+rb)
    pointsA=0
    pointsB=0
    rally=0
    server=random.choice(['a','b'])
    victory=9

    while True:
        r = random.random() 
        if r<p and server=='a':
            pointsA=pointsA+1
        elif r<p and server=='b':
            server='a'
        elif r>=p and server=='b':
            pointsB=pointsB+1
        elif r>=p and server=='a':
            server='b'

        rally+=1
    
        if pointsA == 8 and pointsB == 8:
            victory=random.choice([9,10])
        if pointsA ==victory or pointsB == victory:
            return pointsA,pointsB,rally

def rallies(ra,rb,n):
    ralliesPARS=0
    ralliesENGLISH=0
    

    for i in range(0,n):
        g=gameEnglish(ra,rb)
        f=gamePARS(ra,rb)
        ralliesPARS+=f[2]
        ralliesENGLISH+=g[2]

    ralliesPars_average=ralliesPARS/n
    ralliesEnglish_average=ralliesENGLISH/n
    return ralliesPars_average,ralliesEnglish_average

def winProbabilityPARS(ra,rb,n):
    Awins=0
    Bwins=0
    for i in range(0,n):
        g = gamePARS(ra,rb)
        if g[0]>g[1]:
            Awins+=1
        else:
            Bwins+=1

    prob = Awins/n
    return round(prob,2)

def winProbabilityEnglish(ra,rb,n):
    Awins=0
    Bwins=0
    for i in range(0,n):
        g = gameEnglish(ra,rb)
        if g[0]>g[1]:
            Awins+=1
        else:
            Bwins+=1
    prob = Awins/n
    return round(prob,2)

def file(name):
    listt=[]
    counter=0
    with open(name) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            if counter>=1:
                listt.append((row[0],row[1]))
            counter+=1
        return listt

def mat(list):
    xPARS=[]
    xENGLISH=[]
    yPARS=[]
    yENGLISH=[]

    for i in list: 
        yENGLISH.append(winProbabilityEnglish(int(i[0]),int(i[1]),1000))
        yPARS.append(winProbabilityPARS(int(i[0]),int(i[1]),1000))
        xPARS.append(int(i[0])/int(i[1]))
        xENGLISH.append(int(i[0])/int(i[1]))

    xENGLISH,yENGLISH=zip(*sorted(zip(xENGLISH,yENGLISH)))
    xPARS,yPARS=zip(*sorted(zip(xPARS,yPARS)))

    plt.plot(xENGLISH,yENGLISH,'r',label="ENGLISH")
    plt.plot(xPARS,yPARS,'b',label="PARS")
    plt.ylabel("Probabilities of player A beats player B")
    plt.xlabel("ra/rb")
    plt.legend(loc="lower right")
    plt.title("Comparison between English scoring and PARS methods")
    plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.grid()
    plt.show()
    
def mat_rallies(list):
    xPARS=[]
    yPARS=[]
    xENGLISH=[]
    yENGLISH=[]
    for i in list:
        yPARS.append(rallies(int(i[0]),int(i[1]),1000)[0])
        yENGLISH.append(rallies(int(i[0]),int(i[1]),1000)[1])
        xPARS.append(int(i[0])/int(i[1]))
        xENGLISH.append(int(i[0])/int(i[1]))

    xENGLISH,yENGLISH=zip(*sorted(zip(xENGLISH,yENGLISH)))
    xPARS,yPARS=zip(*sorted(zip(xPARS,yPARS)))
    plt.plot(xENGLISH,yENGLISH,'r',label="ENGLISH")
    plt.plot(xPARS,yPARS,'b',label="PARS")
    plt.ylabel("Rallies")
    plt.xlabel("ra/rb")
    plt.legend(loc="lower right")
    plt.title("Comparison between English scoring and PARS methods rallies")
    plt.grid()
    plt.show()


#print(gamePARS(60,40))
#print(gameEnglish(60,40))
#print(rallies(60,40,100000))
#print(winProbabilityPARS(60,40,100000))
#print(winProbabilityEnglish(60,40,100000))
#mat(file("copy.csv"))
mat_rallies(file("values.csv"))
