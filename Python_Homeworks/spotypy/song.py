class Song: #CONSTRUCTOR    3eqel7w
    def __init__(self, title, releaseYear, duration = 60, likes = 0): # constructor 
        self.__title = title
        self.__releaseYear = releaseYear
        self.__likes = likes
        self.__duration = duration

    def sameSong(self,other): # aux method (it checks if two songs are same ) which is used in album class
        return self.__title == other.__title and self.__duration==other.__duration and self.__releaseYear==other.__releaseYear

    # getters and setters
    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def setDuration(self, duration):
        if self.getDuration() == duration or duration < 0 or duration> 720:
            return False
        self.__duration = duration
        return True

    def getDuration(self):
        return self.__duration

    def getLikes(self):
        return self.__likes
    # end of getters and seters 
    def like(self): # increasing likes by one 
        self.__likes=self.__likes+1
 
    def unlike(self): # decreasing likes by one 
        self.__likes=self.__likes-1
    #toString method returns string ,which contains information about song object*
    def __str__(self) :
        return "Title:"+str(self.getTitle())+",Duration:"+str(self.getDuration()/60)+\
            ",Release year:"+str(self.getReleaseYear())+",Likes:"+str(self.getLikes())


#testing purposes
# rattlestarSong = Song('Snake Jazz', 1989)
# majorSong = Song('Space Oddity', 1969, 315)
# queenSong = Song('Teo Torriatte', 1977, 355, 132178)

# snakeJazz = Song('Snake Jazz', 1989)

# print(snakeJazz.getReleaseYear()) # 1989

# print(snakeJazz.getLikes()) # 0 
# snakeJazz.like()
# print(snakeJazz.getLikes()) # 1

# print(snakeJazz.getDuration()) # 60
# print(snakeJazz.setDuration(324))
# print(snakeJazz.getDuration()) # 90
# print(snakeJazz)
