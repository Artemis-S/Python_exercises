import sys

roman = []
inte = input ("Give a number between 1 and 1000000:")
d = 0
if inte>1000000 or  inte<=0 :
    print ("Inavalid number\n Try again.")

elif inte == 1000000:
    print ("The roman number is -M")

else:
    if inte >= 100000:
        d = inte / 100000
        if d == 9:
            roman.append("-C-M")
        elif d >=5:
            roman.append("-D")
            for i in range (d - 5):
                roman.append("-C")
        elif d == 4:
            roman.append("-C-D")
        elif d >=1 :
            for i in range (d):
                roman.append("-C")
        inte = inte % 100000
    if inte >= 10000:
        d = inte/10000
        if d == 9:
            roman.append("-X-C")
        elif d >= 5 :
            roman.append("-L")
            for i in range (d - 5):
                roman.append("-X")
        elif d == 4:
            roman.append("-X-L")
        elif d >= 1:
            for i in range (d):
                roman.append("-X")
        inte = inte % 10000
    if inte >= 1000:
        d = inte/1000
        if d == 9:
            roman.append("-I-X")
        elif d >=5:
            roman.append("-V")
            for i in range (d - 5):
                roman.append("-I")
        elif d == 4:
            roman.append("-I-V")
        elif d >=1:
            for i in range (d):
                roman.append("M")
        inte = inte % 1000
    if inte >= 100:
        d = inte / 100
        if d == 9:
            roman.append("CM")
        elif d >= 5:
            roman.append("D")
            for i in range (d - 5):
                roman.append("C")
        elif d == 4:
            roman.append("CD")
        elif d >= 1:
            for i in range(d):
                roman.append("C")
        inte = inte % 100
    if inte >= 10 :
        d = inte / 10
        if d == 9 :
            roman.append("XC")
        elif d >= 5 :
            roman.append("L")
            for i in range (d - 5):
                roman.append("X")
        elif d == 4:
            roman.append("XL")
        elif d >=1 :
            for i in range (d):
                roman.append("X")
        inte = inte % 10
    if inte >=1 :
        d = inte
        if d == 9:
            roman.append("IX")
        elif d >=5 :
            roman.append("V")
            for i in range (d - 5):
                roman.append("I")
        elif d == 4:
            roman.append("IV")
        elif d >= 1:
            for i in range (d):
                roman.append("I")
    print("The roman number is: ")
    print "".join(roman)
