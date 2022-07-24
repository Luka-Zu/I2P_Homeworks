# `title` - Title
# * `releaseYear` - The Year it was released
# * `songs`

from song import Song

class Album: # constructor initializes songs with empty list 
    def __init__(self,title,releaseYear) :
        self.__title  = title 
        self.__releaseYear = releaseYear
        self.__songs = []
    # method which adds songs to songs list
    # this method uses var argas ??? if I say it correctly 
    def addSongs(self,*sng):
        added=0
        for x in sng:
            shallAdd=True
            for y in self.__songs:
                if x.sameSong(y):
                    shallAdd=False
            if shallAdd:
                self.__songs.append(x)
                added+=1
        return added
    # counsts total likes of album
    def getToTalLikes(self):
        acumulatorOfLikes=0
        for x in self.getSongs():
            acumulatorOfLikes+=x.getLikes()
        return acumulatorOfLikes

    def getTitle(self):
        return self.__title
    
    def getReleaseYear(self):
        return self.__releaseYear
    
    def getSongs(self):
        return self.__songs
    # followin methods are for sorting songs in album in diffrent variations 
    # i used build in python method for that 
    def sortBy(self, byKey, reverse):
        return sorted(self.getSongs(), key=byKey, reverse=not reverse)
        
    def sortByName(self, reverse):
        return self.sortBy(lambda x: x.getTitle().lower(), reverse)

    def sortByPopularity(self,reverse):
        return self.sortBy(lambda x: x.getLikes(), reverse)

    def sortByDuration(self,reverse):
        return self.sortBy(lambda x: x.getDuration(), reverse)

    def sortByReleaseYear(self,reverse):
        return self.sortBy(lambda x: x.getReleaseYear(), reverse)
    # toString method which contains infromation about album object 
    def __str__(self):
        songs=""
        tempInt=1
        for x in self.getSongs():
            if tempInt==len(self.getSongs()):
                songs+=str(x)
                tempInt+=1
            else:
                songs+=str(x)
                songs+="|"
                tempInt+=1
        return "Title:"+str(self.getTitle())+",Release year:"+str(self.getReleaseYear())+",songs:{"+songs+"}"
# testing 
# j= Album("j",1961)
# print(j.addSongs(Song('A', 2010, 100, 1575), Song('B', 2011, 200, 1570), Song('a', 2012, 300, 7500)))
# print(j)
# x=j.sortByPopularity(False)
# for a in x:
#     print(a)
# print(j.getToTalLikes())
