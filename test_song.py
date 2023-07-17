import unittest 
from Song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song('Kanye West','Jesus Walk',[1])
        self.song2 = Song('Shakira','Waka Waka',2)

    #Test the attributes of Song Object
    def test_init_artist(self):
        """Test that the attribute artist is the same as inputted value when creating the song object"""
        self.assertEqual(self.song1.artist,'Kanye West')
        self.assertEqual(self.song2.artist,'Shakira')
    
    def test_init_title(self):
        """Test that the title attribute is same as inputted value when creating the song object"""
        self.assertEqual(self.song1.title,'Jesus Walk')
        self.assertEqual(self.song2.title,'Waka Waka')
    
    def test_init_tag(self):
        """
        Test that the tag attribute is same as the inputted value
        when creating the song object
        """
        self.assertIsInstance(self.song1.tags,list)
        self.assertEqual(self.song2.tags,2)
    
    def test_add_tags_success(self):
        """
        Test that the new tags are added to the song tag list
        """
        result = self.song1.add_tags('Afrobeats')
        self.assertIn('Afrobeats',self.song1.tags)

    def test_added_tags_failure(self):
        """
        Test when the original tag is not a list. Let it be an integer for example 
        and you want to add tags to the song. This method should
        raise an AttributeError
        """
        self.assertRaises(AttributeError,self.song2.add_tags,"Pop")
       
    def test_str_(self):
        self.assertEqual(self.song1.__str__(),f'{self.song1.artist} - {self.song1.title}')

if __name__ == '__main__':
    unittest.main() 


