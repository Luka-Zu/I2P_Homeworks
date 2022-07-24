from album import Album
from song import Song


class Artist:
    #constructor initializing atributes 
    def __init__(self,firstName,lastName,birthYear,albums,singles):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__birthYear=birthYear
        self.__albums=albums
        self.__singles=singles
    # getters 
    def getFirstName(self):
        return self.__firstName
    def getSecondName(self):
        return self.__lastName
    def getBirthYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__albums
    def getSingle(self):
        return self.__singles   # end of getters

    #method which finds most liked song of the artist
    def mostLikedSong(self):
        cur =None
        curSong= None
        for x in self.__singles: # loop for singles
            if curSong is None:
                curSong=x
                cur=x.getLikes()
            elif cur<x.getLikes():
                cur=x.getLikes()
                curSong=x
        for x in self.getAlbums(): # loop for albums here we need nested for loop 
            for y in x.getSongs():
                if curSong is None:
                    curSong=y
                    cur=y.getLikes()
                elif cur<y.getLikes():
                    cur=y.getLikes()
                    curSong=y
        return curSong
    # simmilar method but it finds least liked song 
    def leastLikedSong(self):
        cur =None
        curSong= None
        for x in self.__singles: # loop for singles
            if curSong is None:
                curSong=x
                cur=x.getLikes()
            elif cur>x.getLikes():
                cur=x.getLikes()
                curSong=x
        for x in self.getAlbums(): # loop for albums here we need nested for loop 
            for y in x.getSongs():
                if curSong is None:
                    curSong=y
                    cur=y.getLikes()
                elif cur>y.getLikes():
                    cur=y.getLikes()
                    curSong=y
        return curSong
    # this method finds sum of all likes
    def totalLikes(self): 
        sum =0 
        for x in self.getAlbums(): # one loop for albums 
            for y in x.getSongs():
                sum+=y.getLikes()
        for x in  self.__singles: # second for singles
            sum+=x.getLikes()
        return sum
    # 'Name: {firstName} {lastName},Birth year:{birthYear},Total likes:{total likes of this artist}'
    def __str__(self):
        return "Name: "+str(self.getFirstName())+" "+str(self.getSecondName())+",Birth year:"+str(self.getBirthYear())+",Total likes:"+str(self.totalLikes())
    
    def sameArtist(self,other):
        return self.getBirthYear()== other.getBirthYear() and self.getFirstName()==other.getFirstName() and self.getSecondName()==other.getSecondName()

    

# j= Album("j",1961)
# print(j.addSongs(Song('A', 2010, 100, 1575), Song('B', 2011, 200, 1570), Song('a', 2012, 300, 7500)))

# er= Album("j",1961)
# print(er.addSongs(Song('e', 2010, 100, 1575), Song('r', 2011, 200, 1570), Song('a', 2012, 300, 32)))

# davidBowie= Artist("david","Bowie",1955,[er,j],[Song('B', 2011, 200, 9999),Song('B', 2011, 200, 100001)])
# print(davidBowie.leastLikedSong())
# print(davidBowie)