import random

w = []
add=0

def winner(p,l):
    pl=0
    for k in range(80):
        if pl==5:
            add = k
            return add
            break
        b = random.randint(1,81)
        print b
        #mpeno ston pinaka kai tsekaro ka8e keli
        for i in range(100):
            for j in range(5):
                if p[i][j] == b:
                    p[i][j]=0

        #elegxo an mia grammi=0
        for i in range(100):
            pl = 0
            for j in range(5):
                if p[i][j]==0:
                    pl +=1
            if pl == 5:
                print "bingo! Player number:", i+1
                print "turn:", k + 1
                break


#poses fores 8a epanalif8ei to paixnidi
for i in range(1001):
    #ftiaxno disdiastato 100 grammes 5 stiles
    p = []
    for i in range(100):
        col =[]
        for j in range(5):
            col = random.sample(range(1,81), 5)
            p.append(col)

    l = len(p)
    f = winner(p,l)
    w.append(f)
for h in range(1001):
    add = add + w[h]
av=(add/1000)
print "average:", av
