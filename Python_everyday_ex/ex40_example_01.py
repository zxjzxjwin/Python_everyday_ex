#coding:utf-8
#直接引用：
#lyrics1 = "They rally around the family", "With pockets full of shells"

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def print_lyrics(self):
        for line in self.lyrics:
            print line

instance1 = Song(["They rally around the family", "With pockets full of shells"])
instance1.print_lyrics()

#间接引用（with as 结构 ）:
#lyrics1 = "They rally around the family", "With pockets full of shells"

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
        
    def __enter__(self):
        return self
        
    def __exit__(self, a, b, c):
        pass
       
    def print_lyrics(self):    
        for line in self.lyrics:
            print line

with Song(["They rally around the family", "With pockets full of shells"]) as instance1:
    instance1.print_lyrics()
	
#将歌词放进变量(token)里:
#lyrics1 = "They rally around the family", "With pockets full of shells"

class Song(object):
    def __init__(self):
#        self.lyrics = lyrics
        pass
        
#    def __enter__(self):
#       return self
        
#    def __exit__(self, a, b, c):
#        pass
       
    def print_lyrics(self, token):    
        for line in token:
            print line

            
token = ["They rally around the family", "With pockets full of shells"]
		
instance1 = Song()
instance1.print_lyrics(token)
	
#with Song(["They rally around the family", "With pockets full of shells"]) as instance1:
#    instance1.print_lyrics()