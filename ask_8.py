def zero(mylist,l):

    f = 0
    #proto stoixeio
    for i in range(0,len(mylist)-2):
        sum = mylist[i]
        #deutero stoixeio
        for j in range(i+1,len(mylist)-1):
            #trito stoixeio
            for k in range(j+1,len(mylist)):
                if (mylist[i] + mylist[j] + mylist[k] == 0):
                    print(mylist[i],mylist[j],mylist[k])
                    f = 1

    if (f == 0):
        print("it does not exist")


import random
# eisago 30 tixaious ari8mous sthn mylist
mylist = random.sample(xrange(-30,30),30)
l = len(mylist)
print(mylist)
zero(mylist,l)
