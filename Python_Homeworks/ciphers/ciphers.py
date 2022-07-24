# ----------------------Index Sub Cipher----------------------

def encryptIndexSubstitutionCipher(text):
    result= ""
    charCounter =len( str(text) )
    for x in range(0,charCounter):
        temp =text[x]
        if x!= charCounter-1:
            a= ord(temp) -ord('a')+1
        
            if(a>=10):
                result = result + str(a) +" "
            else:
                result = result +"0"+ str(a) +" "    
        else:
            a= ord(temp) -ord('a')+1
        
            if(a>=10):
                result = result + str(a) 
            else:
                result = result +"0"+ str(a) 
    return result



def decryptIndexSubstitutionCipher(text):
    result= ""
    charCounter =len( str(text) )
    temp=0
    if text=="":
        return ""
    for x in range(0,charCounter+1):
    
        if x%3==0:
            temp+=10*int(text[x])
        elif x%3==1:
            temp+=int(text[x])
        else:
            temp=temp+ord('a')-1
            result+=chr(temp)  
            temp=0
    return result
            

# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}

def encryptMorseCode(text):
    result=""
    inte=0
    for x in text:
        inte+=1
        if inte !=len(text):
            result+=morseCode.get(x)
            result+=" " 
        else:
            result+=morseCode.get(x)
    return result        
def decryptMorseCode(text):
    result=""
    morseCodeReversed={}
    for a in morseCode:
        morseCodeReversed[morseCode[a]]=a
    tempInt=0
    tempString=""    
    for tempChar in text:
        tempInt+=1
        if(tempChar != " " ) :
            tempString+=tempChar
        else:
            result+=morseCodeReversed[tempString]
            tempString=""
        if(tempInt==len(text)):
            result+=morseCodeReversed[tempString]
    return result
    
# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    result=""
    for x in text:
        tempIntValueForChar= ((ord(x)-ord('a')) * a + b ) % 26
        tempChar= chr(tempIntValueForChar+ord('a'))
        result+=tempChar
    return result    


def decryptAffineCipher(text, a, b):
    result=""
    for x in text:
        tempX = (pow(a,-1,26) * ((ord(x)- ord('a') ) - b)) % 26
        result+=chr(tempX+ord('a'))
    return result    

 
# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    result=""
    k=0

    for x in text:
        
        
        if k%2==0:
            if (ord(x)>=ord('0') and ord(x)<=ord('9')):
                x=(int(str(x))+key1 ) % 10
                result+=str(x)
            elif (    ( ord(x)>=ord('a') and ord(x)<=ord('z')   ) or( ord(x)>=ord('A') and ord(x)<=ord('Z')   )  ):  
                if(ord(x)>= ord('a')):
                    x=  chr(  ( ((ord(x)-ord('a')) +key1 ) % 26)+ord('a')  )
                    result+=str(x)
                else:
                    x=  chr(  ( ((ord(x)-ord('A')) +key1 ) % 26)+ord('A')  )
                    result+=str(x)
            else:
                result+=x      
        else:
            if (ord(x)>=ord('0') and ord(x)<=ord('9')):
                x=(int(str(x))+key2) % 10
                result+=str(x)
            elif ( ( ord(x)>=ord('a') and ord(x)<=ord('z')   ) or( ord(x)>=ord('A') and ord(x)<=ord('Z')   ) ):  
                if(ord(x)>= ord('a')):
                    x=  chr(  ( ((ord(x)-ord('a')) +key2 ) % 26)+ord('a')  )
                    result+=str(x)
                else:
                    x=  chr(  ( ((ord(x)-ord('A')) +key2 ) % 26)+ord('A')  )
                    result+=str(x)
            else:
                result+=x  
        k+=1
    return result
def decryptCaesarCipher(text, key1, key2):
    result=""
    k=0
    for x in text:
        if k%2==0:
            if (ord(x)>=ord('0') and ord(x)<=ord('9')):
                x=(int(str(x))-key1) % 10
                result+=str(x)
            elif (( ord(x)>=ord('a') and ord(x)<=ord('z')   ) or( ord(x)>=ord('A') and ord(x)<=ord('Z')   ) ):  
                if(ord(x)>= ord('a')):
                    x=  chr(  ((ord(x)-ord('a')-key1)%26 ) +ord('a'))
                    result+=str(x)
                else:
                    x=  chr(  ((ord(x)-ord('A')-key1)%26 ) +ord('A'))
                    result+=str(x)
            else:
                result+=x
        else:
            if (ord(x)>=ord('0') and ord(x)<=ord('9')):
                x=(int(str(x))-key2) % 10
                result+=str(x)
            elif (( ord(x)>=ord('a') and ord(x)<=ord('z')   ) or( ord(x)>=ord('A') and ord(x)<=ord('Z')   )  ):  
                if(ord(x)>= ord('a')):
                    x=  chr(  ((ord(x)-ord('a')-key2)%26 ) +ord('a'))
                    result+=str(x)
                else:
                    x=  chr(  ((ord(x)-ord('A')-key2)%26 ) +ord('A'))
                    result+=str(x)
            else:
                result+=x
        k+=1
    return result

# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    result=""
    tempString=""
    firstList=[]
    tempInt = 0
    
    for x in text:
        tempInt+=1
        tempString+=x
        if(tempInt%key==0 or tempInt==len(text)):
            firstList.append(tempString)
            tempString=""
    secondList=[]
    x = 0
    
    for a in range(1,key+1):
        tempString=""

        for b in firstList:
            if(len(b) > x):
                tempString+=b[x]
                
        secondList.append(tempString)
        x+=1
    
    
    for a in secondList:
        result+=a
    return result        




def decryptTranspositionCipher(text, key):
    result= ""
    tempInt=0
    tempString=""
    secondList=[]
    if key!=0:
        x=len(text)//key 
        y=len(text)%key 
    notHasExtra=True
    for a in text:

        if tempInt<x:
            tempString+=a
            tempInt+=1
        elif y!=0 and notHasExtra:
            y-=1
            notHasExtra=False
            tempString+=a
        else:
            secondList.append(tempString)
            tempString=a
            notHasExtra=True
            tempInt=1
    secondList.append(tempString)    
        
    for a in range(0,len(secondList[0])):
        for b in secondList:
            if a<len(b):
                result+=b[a]
    return result
