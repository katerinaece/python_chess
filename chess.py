from functions import findprevious, checkifstart
from lists import board

start = input("Type the START position: ")
print("You chose ", start, " for start position")

end = input("Type the END position: ")
print("You chose ", end, " for end position")

steps = input("Type the number of steps: ")
print("You chose ", steps, " number of steps")
steps = int(steps)

if steps == 1:
    a=findprevious(board,end)
    a1=checkifstart(a,start)
    if a1 == 1:
        print(start,"-->",end)
    

if steps == 2:
    a=findprevious(board,end)
    a1=checkifstart(a,start)
    if a1 == 1:
        print(start,"-->",end)
    for k in range(1,len(a)):
        b=findprevious(board,a[k])
        b1=checkifstart(b,start)
        if b1 == 1:
            print(start,"-->",a[k],"-->",end)
            
            
if steps == 3:
    a=findprevious(board,end)
    a1=checkifstart(a,start)
    if a1 == 1:
        print(start,"-->",end)
    for k in range(1,len(a)):
        b=findprevious(board,a[k])
        b1=checkifstart(b,start)
        if b1 == 1:
            print(start,"-->",a[k],"-->",end)
        for i in range(1,len(b)):
            c=findprevious(board,b[i])
            c1=checkifstart(c,start)
            if c1 == 1:
                print(start,"-->",b[i],"-->",a[k],"-->",end)
            
if steps == 4:
    a=findprevious(board,end)
    a1=checkifstart(a,start)
    if a1 == 1:
        print(start,"-->",end)
        path.append([start,end])
    for k in range(1,len(a)):
        b=findprevious(board,a[k])
        b1=checkifstart(b,start)
        if b1 == 1:
            print(start,"-->",a[k],"-->",end)
        for i in range(1,len(b)):
            c=findprevious(board,b[i])
            c1=checkifstart(c,start)
            if c1 == 1:
                print(start,"-->",b[i],"-->",a[k],"-->",end)
            for j in range(1,len(c)):
                d=findprevious(board,c[j])
                d1=checkifstart(d,start)
                if d1 == 1:
                    print(start,"-->",c[j],"-->",b[i],"-->",a[k],"-->",end)
                
input('Press ENTER to exit')
