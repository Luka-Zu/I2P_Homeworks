from random import randint # Do not delete this line

def displayIntro():
    fileForIntro=open("intro.txt","r")
    print(fileForIntro.read())
    fileForIntro.close()

def displayEnd(result):
    if result:
        winning=open("winnerDisplay.txt","r")
        print(winning.read())
        winning.close()
    else:
        losing=open("losingDisplay.txt","r")
        print(losing.read())
        losing.close()   
    
            
def displayHangman(state):
    if state==5:
        staten=open("state5.txt","r")
        print(staten.read())
        staten.close()
    elif state==4:
        staten=open("state4.txt","r")
        print(staten.read())
        staten.close()
        
    elif state==3:
        staten=open("state3.txt","r")
        print(staten.read())
        staten.close()
       
    elif state==2:
        staten=open("state2.txt","r")
        print(staten.read())
        staten.close()
     
    elif state==1:
        staten=open("state1.txt","r")
        print(staten.read())
        staten.close()

    if state==0:
        staten=open("state0.txt","r")
        print(staten.read())
        staten.close()

def getWord():
    fileToBeOpened=open("hangman-words.txt","r")
    lst=fileToBeOpened.readlines()
    randomint=randint(0,len(lst))
    fileToBeOpened.close()
    return lst[randomint]


def valid(c):
    if len(c)!=1:
        return False
    else:
        return ord(c)>=ord("a") and ord(c)<=ord("z")


def play():
    toGuess=getWord()
    lives=5 
    word=[]
    intTemp=0
    for a in toGuess:
        intTemp+=1
        if(intTemp!=len(toGuess)-1):
            word.append("*")
    alreadUsed=[]
    needsToGuess=len(toGuess)    
    while(lives>0 and needsToGuess-1>0):
        
        displayHangman(lives)
    
        str1 = ''.join(word)
        print("Guess the word:",str1)
        temp=""
        n=True
        while n:
            temp=input("Enter the letter:")
            
            if valid(temp) and not(temp in alreadUsed):
                tempInt=0
                isNotOne=True
                for b in toGuess:
                    if b == temp:
                        alreadUsed.append(temp)
                        word[tempInt]=temp
                        needsToGuess-=1
                        isNotOne=False
                    tempInt+=1
                if isNotOne:
                    lives=lives-1    
                n=False 
            else:
                if temp in alreadUsed:
                    print("this was already used,pick diffrent char")
                else:
                    print("invalid letter, please input again")  
             
    print("The word was:",toGuess)
    if lives==0:
        displayHangman(0)   
    return lives>0            
                

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        a=input("if you want to end game then type (no) \n type anything else to continue!")
        if a=="no":
            return

if __name__ == "__main__":
    
    hangman()

