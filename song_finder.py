"""
CS 5001
Project 4: Data Processing Json file, Classses and Data Structures
Name: Princewill Umeh
"""
import json
import os
import sys
from Song import Song
from Library import Song_Library

def get_json_list_path(directory):
    """
    File Traversal function
    """
    list_json_path = [] #created a list containing all the json files paths
    for roots, dirs, sublist in os.walk(directory):
        for file in sublist:
                if file.endswith('.json'):
                     list_json_path.append(os.path.join(roots, file))
        
    return list_json_path #there are 9330 music tracks in json format

def load_json(json_path):
    """
    This function loads all the json files
    input: List of file paths containing each json file
    return: List of dictionaries containing each song's information
    """
    json_list = []
    for file in json_path:
        open_json_file = open(file)
        json_dict = json.load(open_json_file)
        json_list.append(json_dict)
    return json_list

def get_song_to_library(json_lists,song_library):
    """
    This function creates song objects and adds them to the Song Library object.
    input: list of dictionaries containing each song's information, and a Song Library object
    returns: the song library object which is a list of songs
    """
    for i in range(len(json_lists)):
        song_tags= []
        artist = json_lists[i]['artist']
        title = json_lists[i]['title']
        tag_list =json_lists[i]['tags']
        track_id = json_lists[i]['track_id']
        similars = json_lists[i]['similars']
        #get the tags from the nested list of tags in the json file
        for j in range(len(tag_list)):
             song_tags.append(tag_list[j][0])
        song = Song(artist,title,song_tags,track_id)
        song_library.add_song(song)
        
        for k in range(len(similars)):
             song.add_similars(similars[k][0])
                 
    return song_library

def add_new_song_to_library(song,song_library):
     """
     This function adds a new song to the library.
     """
     song_library.add_song(song)
     return song_library

def search_by_artist(song_library, artist):
     """
     This function searches the song library data structure by artist
     input: the Song library data structure, and the artist name 
     returns: A list of song titles
     """
     return song_library.search_by_artist(artist) 
     
def search_by_tags(song_library,tag):
     """
     This function searches the song library data structure by tag
     input: the Song library data structure, and the tag name
     returns: A list of song 
     """
     return song_library.search_by_tags(tag)

def get_tag_frequency(song_library):
     """
     This function seach for the most popular tag by frequency
     input: the song library data structure
     returns: a sorted list of the top 10 tags
     """
     return song_library.get_most_popular_tags()

def get_artist_n_songs(song_library,number_of_songs):
     """
     This function search for artist that have more than n songs. 
     N is the number of songs specified in the parameter

     input: the song library object, an artist_song dictinary, the number of songs
     returns: a dictionary of artist names as the keys and the list of songs as the values
     """
     try: 
          return song_library.show_artist_with_n_songs(number_of_songs)
     except ValueError as e: 
          print(e)
          
def get_tags_n_songs(song_library,number_of_songs):
     """
     This function search for tag that have more than n songs. 
     N is the number of songs specified in the parameter

     input: the song library object, the number of songs
     returns: a dictionary of tags as the keys and the list of songs as the values
     """
     try: 
          return song_library.show_tags_with_n_songs(number_of_songs)
     except ValueError as e:
          print(e)

def display_song_list(list,header):
     """
     Prints the search by artsit and search by tag features in 
     a nice format
     """
     print(f'Search: {header}\n')
     for item in list:
          print(f'\t{item.title}')

def display_song_frequency(list):
     """
     Prints the most popular tags in a nice format
     """
     print('Top 10 tags:\n')
     for item in list:
          print(f'\t{item[0]} - {item[1]}') 

def display_n_songs(dictionary, header, number_of_songs):
     """
     Prints the Show artist n song and Show tag n song 
     features in a nice format
     """
     print(f'{header} with more than {number_of_songs} songs:\n')
     print("")
     for key, value in dictionary.items():
          print(f'\t{key}:{value}\n')
          print("")

# def main(): 
#     json_path = get_json_list_path("lastfm_subset")
#     json_list = load_json(json_path)
#     Library1 = Song_Library() # this is a list
#     song_library = get_song_to_library(json_list,Library1)
#     similar_song = song_library.track_id_to_song()
#     print(len(similar_song))
#     song_library.track_id_dict
#     print(song_library.library[1].artist)
#     print(song_library.library[1].title)
#     print(similar_song["TRAAAAW128F429D538"])


#     choice = True
#     while choice:
#           print(
# """
# Menu to search the Song Library (Select a number between 1 and 6): 

# 1. search by artist
# 2. search by tag
# 3. get the most popular tag
# 4. Show artist with n number of songs
# 5. Show tags with n number of songs
# 6. Exit the program
# """
#           )
#           try:
#                selection = int(input("How do you want to search the song library? ").strip())
#                if selection == 1:
#                     artist = input('Which artist are you interested in? ').strip()
#                     try:
#                          result = search_by_artist(song_library,artist)
#                          display_song_list(result,artist)
#                     except KeyError:
#                          print("\nArtist not found")
#                elif selection == 2: 
#                     tag = input('What tags do you want to search for? ').strip()
#                     try:
#                          result = search_by_tags(song_library,tag)
#                          display_song_list(result,tag)
#                     except KeyError:
#                          print("\nTag not found")
#                elif selection == 3:
#                     result = get_tag_frequency(song_library)
#                     display_song_frequency(result)
#                elif selection == 4:
#                     number_of_songs = int(input('Enter a number of songs: ').strip())
#                     result = get_artist_n_songs(song_library,number_of_songs)
#                     header = 'Artist'
#                     display_n_songs(result,header,number_of_songs)
#                elif selection == 5: 
#                     number_of_songs = int(input('Enter a number of songs: ').strip())
#                     result = get_tags_n_songs(song_library,number_of_songs)
#                     header = 'Tags'
#                     display_n_songs(result,header,number_of_songs)
#                elif selection == 6: 
#                     sys.exit('User has terminated their search')
#                else: 
#                     print('\nInvalid selection')
#                     continue
#           except ValueError:
#                print("\nThe inputed selection must be an integer")
       

# main()