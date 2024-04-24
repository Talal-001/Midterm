class Song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration
    def get_song(self):
        return self.title,self.artist,self.duration
class Playlist(Song):
    def __init__(self,title,description):
        self.description=description
        self.title=title
        self.listofsong=[]
    def insert_song(self,song):
        return self.listofsong.append(song)
    def remove_song(self,song):
        return self.listofsong.pop(song)
    def display_songobjects(self):
        return self.listofsong
    def display_playlist(self):
        return self.description,self.title,self.listofsong
class Library(Playlist):
    def __init__(self):
        self.listofplaylist=[]
    def insert_playlist(self,playlitss):
        return self.listofplaylist.append(playlitss)
    def remove_playlist(self,playlist):
        return self.listofplaylist.pop(playlist)
    def display_playlistss(self):
        return self.listofplaylist
    
song1=Song('Started from the bottom','Drake','4:56')
song2=Song('Hotlinebling','Drake','6:56')
song3=Song('Members','Drake','3:56')
song4=Song('Part i','4batz','2:56')
print(song1.get_song())
print(song2.get_song())
print(song3.get_song())
print(song4.get_song())

playlist1=Playlist("...",'Sleeping')
playlist2=Playlist("Bored",'When bored')
playlist1.insert_song(song1)
playlist1.insert_song(song2)
playlist2.insert_song(song3)
playlist2.insert_song(song4)
playlist1.display_songobjects()
playlist2.display_songobjects()

lib1=Library()
lib1.insert_playlist(playlist1)
lib1.insert_playlist(playlist2)
lib1.display_playlistss()
