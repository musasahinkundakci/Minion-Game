def minion_game(string):
    pointA=0
    pointB=0
    stringlist=list(string)
    sayac=0
    for i in stringlist:
        if(i.lower()=="a" or i=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u"):
            
            pointA+=len(stringlist)-sayac
            
        else:
            pointB+=len(stringlist)-sayac
               
        sayac+=1   
    if(pointA>pointB):
        print("Kevin {}".format(pointA))
    else:
        print("Stuart {}".format(pointB))
                

if __name__ == '__main__':
    s = input()
    minion_game(s)
