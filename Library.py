from Song import Song
class Song_Library: 
    def __init__(self):
        self.library = []
        self.artist_dict = {}
        self.tag_dict = {}
        self.track_id_dict = {}

    def add_song(self,song):
        self.library.append(song)
        if song.artist in self.artist_dict:
            self.artist_dict[song.artist].append(song)
        else:
            self.artist_dict[song.artist] = [song]

        for i in range(len(song.tags)):
               if song.tags[i] in self.tag_dict:
                    self.tag_dict[song.tags[i]].append(song)
               else:
                    self.tag_dict[song.tags[i]] = [song]
        #this method is will be adding song to the various data structures
    def track_id_to_song(self):
        for song in self.library: 
            self.track_id_dict[song.track_id] = song
        return self.track_id_dict
    def search_by_artist(self, artist = str):
        artist_songs = self.artist_dict[artist]
        return artist_songs
    
    def search_by_tags(self,tag):
        tag_songs = self.tag_dict[tag]
        return tag_songs
    
    def get_most_popular_tags(self):
        tag_frequency_dict = {}  
        for song in self.library: 
            for tag in song.tags:
                if tag in tag_frequency_dict:
                    tag_frequency_dict[tag] +=1
                else: 
                    tag_frequency_dict[tag] = 1
        
        #The Sorted function code adapted from 
        # https://sparkbyexamples.com/python/sort-list-of-tuples-in-python/
        sorted_tag_frequency = sorted(tag_frequency_dict.items(), key=lambda x:x[1],reverse=True)
        return sorted_tag_frequency[0:10]
    
    def show_artist_with_n_songs(self,number_of_songs = int): 
        artist_with_n_songs_dict = {}
        for key ,value in self.artist_dict.items():
            if len(value) >= number_of_songs:
                artist_with_n_songs_dict[key] = value
        return artist_with_n_songs_dict
    
    def show_tags_with_n_songs(self,number_of_songs = int):
        tags_with_n_songs_dict = {}
        for key, value in self.tag_dict.items():
            if len(value) >= number_of_songs:
                tags_with_n_songs_dict[key] = value
        return tags_with_n_songs_dict


