s="."
d=0
tg=0
while (s!="") :

    s=input()
    if(s=="A_plus") :
        d=d+1
        tg=tg+4
    if(s=="A") :
        d=d+1
        tg=tg+4
    if(s=="A-") :
        d=d+1
        tg=tg+3.7
    if(s=="B+") :
        d=d+1
        tg=tg+3.3

    if(s=="B") :
        d=d+1
        tg=tg+3

    if(s=="B-") :
        d=d+1
        tg=tg+2.7

    if(s=="C+") :
        d=d+1
        tg=tg+2.3
    if(s=="C") :
        d=d+1
        tg=tg+2
    if(s=="C-") :
        d=d+1
        tg=tg+1.7
    if(s=="D+") :
        d=d+1
        tg=tg+1.3
    if(s=="D") :
        d=d+1
        tg=tg+1
    if(s=="F") :
        d=d+1
print(tg/d)