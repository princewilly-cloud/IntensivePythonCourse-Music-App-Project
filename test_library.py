import unittest
from Library import Song_Library
from Song import Song

song_title = ['King Kunta','Last Last','Alright','Essence','Technologic','Ye','When I Pray','Fever','2 Sugar','On the Low']
song_artist = ['Kendrick Lamar','Burna Boy','Kendrick Lamar','Wizkid','Daft Punk','Burna Boy','DOE','Wizkid','Wizkid','Burna Boy']
tag = ['Hip-Hop','afrobeat','Hip-Hop','afrobeat','House','afrobeat','Christian','afrobeat','afrobeat','afrobeat']

class TestLibrary(unittest.TestCase):
    def setUp(self):
        #Set up an instance of a song library and a song before testing
        self.library1 = Song_Library()
        self.song1 = Song('Kanye West','Jesus Walk', ['Hip-Hop'] )

        Song_Object_List = []
        #Create a list of song objects and add them to the library
        if len(song_title) == len(song_artist) == len(tag):
            for i in range(len(song_title)):
                song = Song(song_artist[i],song_title[i],[tag[i]])
                Song_Object_List.append(song)
        for song in Song_Object_List:
            self.library1.add_song(song)

    def test_init_library(self):
        """Test the attributes of the Song Library object. the library should be a list"""
        self.assertIsInstance(self.library1.library, list)

    def test_add_song(self):
        """Test adding a song to the library"""
        self.library1.add_song(self.song1)

        #Check that the title of the latest song  we added to the library
        #is the same as the title attribute of Song1
        self.assertEqual(self.library1.library[-1].title, self.song1.title)
    
    def test_search_by_artist_success(self):
        """
        Test for when the artist is searchable. 
        Return: a list of the artist songs title
        """
        Artist_song_dict ={}
        for song in self.library1.library:
            if song.artist in Artist_song_dict: 
                Artist_song_dict[song.artist].append(song.title)
            else:  
                Artist_song_dict[song.artist] = [song.title] 
        result = self.library1.search_by_artist(Artist_song_dict,'Burna Boy')
        self.assertEqual(len(result),3)

    def test_search_by_artist_failure(self):
        """Test for when the artist is not in the library. This method should raise 
           a Key Error exception
        """
        Artist_song_dict ={}
        for song in self.library1.library:
            if song.artist in Artist_song_dict: 
                Artist_song_dict[song.artist].append(song.title)
            else:  
                Artist_song_dict[song.artist] = [song.title] 
        self.assertRaises(KeyError,self.library1.search_by_artist, Artist_song_dict,'1')
    
    def test_search_by_tag_succes(self):
        """
        Test for when the tag is searchable
        Return: a list of of the song title 
        """
        Tag_song_dict = {}
        for song in self.library1.library:
            for i in range(len(song.tags)):
               if song.tags[i] in Tag_song_dict:
                    Tag_song_dict[song.tags[i]].append(song.__str__())
               else:
                    Tag_song_dict[song.tags[i]] = [song.__str__()]

        result = self.library1.search_by_tags(Tag_song_dict,'afrobeat')
        self.assertEqual(len(result),6)
    
    def test_search_by_tags_failure(self):
        """Test for when the tag is not searchable. Raise a KeyError"""
        Tag_song_dict = {}
        for song in self.library1.library:
            for i in range(len(song.tags)):
               if song.tags[i] in Tag_song_dict:
                    Tag_song_dict[song.tags[i]].append(song.__str__())
               else:
                    Tag_song_dict[song.tags[i]] = [song.__str__()]
        self.assertRaises(KeyError,self.library1.search_by_tags,Tag_song_dict,'Mising_1')

    def test_get_most_popular_tags_success(self):
        """ 
        Test for when there are less than 10 tags. for example 4 tags.
        The result will return the top 4 tags by frequency
        """
        result = self.library1.get_most_popular_tags()
        self.assertTrue(len(result) == 4)

    def test_get_most_popular_tags_failure(self):
        """
        Test for when there are less than 10 tags. 
        The result should not return the top 10 tags (the default).
        Rather it should return top n tags (where n is less than 10).
        """
        result = self.library1.get_most_popular_tags()
        self.assertFalse(len(result) == 10)

    def test_show_artist_with_n_songs_success(self):
        """
        Test for when the number of songs is an integer. 
        The result should return a dictionary
        """
        Artist_song_dict ={}
        for song in self.library1.library:
            if song.artist in Artist_song_dict: 
                Artist_song_dict[song.artist].append(song.title)
            else:  
                Artist_song_dict[song.artist] = [song.title] 
        result = self.library1.show_artist_with_n_songs(Artist_song_dict,10)
        self.assertIsInstance(result,dict)

    def test_show_artist_with_n_songs_failure(self):
        """
        Test for when the number of songs is a string.
        the result will raise a TypeError
        """
        Artist_song_dict ={}
        for song in self.library1.library:
            if song.artist in Artist_song_dict: 
                Artist_song_dict[song.artist].append(song.title)
            else:  
                Artist_song_dict[song.artist] = [song.title] 
        self.assertRaises(TypeError, self.library1.show_artist_with_n_songs,Artist_song_dict,'10')
    
    def test_show_tags_with_n_songs_success(self):
        """
        Test for when the number of songs is an integer. 
        The result should return a dictionary
        """
        Tag_song_dict = {}
        for song in self.library1.library:
            for i in range(len(song.tags)):
               if song.tags[i] in Tag_song_dict:
                    Tag_song_dict[song.tags[i]].append(song.__str__())
               else:
                    Tag_song_dict[song.tags[i]] = [song.__str__()]
        result = self.library1.show_tags_with_n_songs(Tag_song_dict,280)
        self.assertIsInstance(result,dict)

    def test_show_tags_with_n_songs_failure(self):
        """
        Test for when the number of songs is a string.
        the result will raise a TypeError
        """
        Tag_song_dict = {}
        for song in self.library1.library:
            for i in range(len(song.tags)):
               if song.tags[i] in Tag_song_dict:
                    Tag_song_dict[song.tags[i]].append(song.__str__())
               else:
                    Tag_song_dict[song.tags[i]] = [song.__str__()]
        self.assertRaises(TypeError, self.library1.show_tags_with_n_songs,Tag_song_dict,'280')
   
if __name__ == '__main__':
    unittest.main() 

