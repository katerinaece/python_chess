def findprevious(board,dest):   #dineis ena tetragwno kai soy leei me poia sindeetai
    for i in range(len(board)):        
        if board[i][0] == dest:
##            print("pws tha paw sto ", dest, "-->",board[i])
            break
    return board[i]

def checkifstart(a,start): #dineis to start kai leei an luthike to problhma
    flag = 0
    
    for i in range(1,len(a)):        
        if a[i] == start:
            flag = 1
            break
    return flag
