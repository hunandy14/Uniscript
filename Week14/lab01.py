import random
import numpy as np

randint=random.randint
sc=[0,0,0]

def s0():
    global sc
    sc[0]+=1
    return 1

def  s1():
    global sc
    sc[1]+=1
    if randint(0,100)<10:
        return 0
    return 2

def  s2():
    global sc
    sc[2]+=1
    dice=randint(0,100)
    if dice<20:
        return 1
    elif dice<50:
        return 2
    return 0

def sim(n):
    global sc
    sc=[0,0,0]
    cs=0
    for s in range(n):
        if cs==0:
            cs=s0()
        elif cs==1:
            cs=s1()
        else:
            cs=s2()
    return sc

if __name__=="__main__":
    a=np.array(sim(50000))
    print "Visited         : %s" % str(a)
    print "State Prob.  : %s" % str(a*1.0/sum(a))