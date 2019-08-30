for x in range(1,11):
     input()
    T=input();d=[];l=[]
    for i in T:
        if i.isdigit():l += [int(i)]
        elif i==")":
        j=-1
    while d[j]!="(":
            if d[j]=="*":l[j-1]=l[j-1]*l[j];l.pop(j);d.pop(j)
        else:j-=1
    j=-1
        while d[j]!="(":
            if d[j]=="+":l[j-1]=l[j-1]+l[j];l.pop(j);d.pop(j)
            else:j-=1
        d.pop(-1)
    else:d+=[i]
    print("#%d %d"%(x,l[0]))


