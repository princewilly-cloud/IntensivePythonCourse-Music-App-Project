class Song:
    def __init__(self,artist = str,title = str,tag_list = list, track_id = str): 
        self.artist = artist
        self.title = title
        self.tags = tag_list
        self.track_id = track_id
        self.similars = []
        
    def add_tags(self,tag):
        self.tags.append(tag)
    def add_similars(self,song_id):
        self.similars.append(song_id)
    def __str__(self): 
        return f'{self.artist} by {self.title}'
    