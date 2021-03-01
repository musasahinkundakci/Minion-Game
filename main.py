def minion_game(string):
    listedstring=list(string)
    sayac=0
    kevin=0
    stuart=0
    for i in listedstring:
        if(i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="u" or i.lower()=="o"):
            kevin+=len(listedstring)-sayac
        
        else:
            stuart+=len(listedstring)-sayac
            
        sayac+=1
    if(stuart>kevin):
        print( "Stuart {}".format(stuart))
    elif(kevin>stuart):
        print("Kevin {}".format(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
