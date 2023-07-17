"""
CS 5001
Project 5: Song Web Application
Name: Princewill Umeh
"""
#Import classes, modules and and methods
import json
import os
from Song import Song
from Library import Song_Library
from flask import Flask
from flask import render_template
from flask import request
from song_finder import get_json_list_path,load_json,get_song_to_library

#Get the list of file directories containing the json files
json_path = get_json_list_path("lastfm_subset")
#This function loads all the json files
json_list = load_json(json_path)
Library1 = Song_Library() # this is a list
#the song library data structure
song_library = get_song_to_library(json_list,Library1)
similar_dict = song_library.track_id_to_song()

app = Flask(__name__)

#The home page to search for music by artist, or tag
@app.route('/')
@app.route('/songfinder/', methods=['GET'])
def songfinder(): 
        search_type = request.args.get('search_type')
        artist = request.args.getlist('query')
        tag = request.args.getlist('query')
        popular_tag = song_library.get_most_popular_tags()

        if search_type == 'artist' and len(artist)> 0: 
            try:
               result = song_library.artist_dict[artist[0].strip()]
               return render_template('songfinder.html',items = result, query = artist[0],search_type = search_type, popular = popular_tag)
            except:
                render_template('songfinder_no_search.html', popular = popular_tag) #returns to a new search if a search error occurred
        elif search_type == 'tag' and len(tag) > 0:
            try:
               result = song_library.tag_dict[tag[0].strip()]
               return render_template('songfinder_tag.html',items = result, query =tag[0], search_type = search_type, popular = popular_tag)
            except:
                 render_template('songfinder_no_search.html', popular = popular_tag) #returns to a new search if a search error occurred
        return render_template('songfinder_no_search.html', popular = popular_tag)

#Route to the artist page, which shows all the artist's songs
@app.route('/artist_page/', methods = ['GET'])
def artist_page(): 
     artist = request.args.get('artist')
     if len(artist) > 0: 
          result = song_library.search_by_artist(artist.strip())
          return render_template('artist_page.html', items = result)
     
#Route to the song page to see the song information
@app.route('/song_info/', methods = ['GET'])
def song_info():
     track_id = request.args.get('track_id')
     similar_song_obj = []
     if len(track_id) > 0:
          for song in song_library.library:
               if song.track_id == track_id:
                result = song
                similar = song.similars
                break
          for track in similar:
               if track in similar_dict.keys():
                    similar_song_obj.append(similar_dict[track])
     return render_template('song_info.html', items= result, similars = similar_song_obj)
     
#Route to the popular tag page to see the songs for each popular tag, the user selected
@app.route('/popular/', methods = ['GET'])
def popular():
     tag = request.args.get('tag')
     if len(tag) > 0:
          result = song_library.search_by_tags(tag)
          return render_template('popular_tags.html', items = result, query = tag)
         
if __name__ == '__main__':
    app.run(debug=True)



    













