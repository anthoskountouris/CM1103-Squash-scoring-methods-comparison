import random
import math
import csv
import matplotlib.pyplot as plt

def game(ra,rb):
    p=ra/(ra+rb)
    pointsA=0
    pointsB=0

    while True:
        r = random.random() 
        if r<p:
            pointsA=pointsA+1
        else:
            pointsB=pointsB+1

        if (math.fabs(pointsA-pointsB)>=2) and (pointsA>=11 or pointsB>=11) :
            return pointsA,pointsB


def winProbability(ra,rb,n):
    Awins=0
    Bwins=0
    for i in range(0,n):
        g = game(ra,rb)
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
    div=[]
    prob=[]
    for i in list: 
        prob.append(winProbability(int(i[0]),int(i[1]),10000))
        div.append(int(i[0])/int(i[1]))

    div,prob=zip(*sorted(zip(div,prob)))

    plt.plot(div,prob,'r')
    plt.ylabel("Probabilities of player A beats player B")
    plt.xlabel("ra/rb")
    plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.grid()
    plt.show()

def one_e():
    p=winProbability(60,40,100000)
    if p>0.90:
        return 1
    else:
        for n in range(2,100):
            pl=0
            for i in range(0,(2*n-1)):
                if i==0:
                    pl+=(p**n)*((1-p)**(i))
                else:
                    pl+=(p**n)*((1-p)**(i))*(math.factorial(n)/(math.factorial(n-1)*math.factorial(n-(n-1))))
            print(f"n ->{n} == probability: {pl}")
            if pl>=0.9:
                return n
            
            
#print(game(70,30))
#print(winProbability(70,30,100000))
#print(file("test.csv"))
#mat(file("test.csv"))
#print(one_e())

