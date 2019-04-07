import random
from tabulate import tabulate
import matplotlib.pyplot as plt
import json
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import eyed3
import datetime


class Song:
    def __init__(self, title, artist, album, length):
        self.init_data_validation(title, artist, album, length)

        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    @property
    def length(self):
        return self.__length

    def __str__(self):
        return "{" + str(self.artist)+"} - {" + str(self.title) + "} from {" + str(self.album)+ "} - {"+str(self._length)+"}"

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self._length == other._length

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))


    def length(self, seconds = False, minutes = False, hours = False):
        time_parts = self._length.split(':')
        print(time_parts)
        if len(time_parts) == 2:
            length_in_seconds = int(time_parts[1]) + int(time_parts[0])*60
            length_in_minutes = int(time_parts[0])
            length_in_hours = 0
        if len(time_parts) == 3:
            length_in_hours = int(time_parts[0])
            length_in_minutes = int(time_parts[0])*60 + int(time_parts[1])
            length_in_seconds = int(time_parts[2]) + int(length_in_minutes*60)
        if seconds:
            return length_in_seconds
        if minutes:
            return length_in_minutes
        if hours:
            return length_in_hours
        else:
            return(str(self._length))
            

    def init_data_validation(self, title, artist, album, length):
        if not isinstance(title, str) or not isinstance(artist, str) or not isinstance(album, str):
            raise TypeError('you try to input wrong type of data, please try again ')
        
            #TODO validation for length
            #raise InputError("Length should be in time format hours:minutes:seconds")


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.__songs = []
        self._played_songs = []

        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, song):
        for songs in self.__songs:
            if songs.title == song.title:
                self.__songs.remove(song)
        else:
            print('that song do not exist in playlist')
    
    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total_length_in_seconds = 0
        for song in self._Playlist__songs:
            total_length_in_seconds += song.length(seconds=True)

        m, s = divmod(total_length_in_seconds, 60)
        h, m = divmod(m, 60)
        return '{:d}:{:02d}:{:02d}'.format(h, m, s)

    def count_of_songs(self, artist):
        count_of_songs_for_artist = 0
        for song in self.__songs:
            if song.artist == artist:
                count_of_songs_for_artist += 1
        return count_of_songs_for_artist

    def artists(self):
        dictionary = {}

        for song in self.__songs:
            songs = self.count_of_songs(song.artist)
            dictionary.update({song.artist:songs})
        #TODO да погледмна, защо не ми дава да чертая histograma използвайки 
        #библиотеката matplotlib
        plt.bar(dictionary.keys(), dictionary.values(), width=0.2, color='g')
        return plt.show()

    def next_song(self):
        if len(self._played_songs) == len(self.__songs):
            if self.repeat == True:
                if self.shuffle == False:
                    song_to_play = self.__songs[0]
                    self._played_songs = [song_to_play]
                else:
                        index = random.randint(0,3)
                        song_to_play = self.__songs[index]
                        self._played_songs = [song_to_play]
    
            else:
                print("there is no more songs in playlist")
        else:
            if self.shuffle == False:
                    song_to_play = self.__songs[len(self._played_songs)]
                    self._played_songs .append(song_to_play)
            else:
                while(True):
                    index = random.randint(0,len(self.__songs) - 1)
                    if not self.__songs[index] in self._played_songs:
                        song_to_play = self.__songs[index]
                        self._played_songs.append(song_to_play)
                        break
        return song_to_play

    def pprint_playlist(self):
        array=[]
        for song in self.__songs:
           sub_arr=[song.artist,song.title,song._length]
           array.append(sub_arr)
        print(tabulate(array, headers=['Artist', 'Song','Length'], tablefmt='orgtbl'))

    def save(self):
        splited_playlist_name = self.name.split(' ')
        if len(splited_playlist_name) > 1:
            file_name = ('-').join(splited_playlist_name)
        else:
            file_name = self.name

        json_dictionary = {song.title:(song.artist, song.album,song._length) for song in self.__songs}

        with open(file_name, 'w') as outfile:  
            json.dump(json_dictionary, outfile)

    @staticmethod
    def load(path):
        with open(path) as json_file:  
            data = json.load(json_file)
        path_without_dot_json = path[:-5]
        splited_path = path_without_dot_json.split('-')
        if len(splited_path) > 1:
            playlist_name = (' ').join(splited_path)
        else:
            playlist_name = path_without_dot_json
        new_playlist = Playlist(playlist_name)
        list_of_songs = []
        for key, val in data.items():
            song = Song(key, val[0], val[1], val[2])
            list_of_songs.append(song)
        new_playlist.add_songs(list_of_songs)
        return new_playlist

class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def generate_playlist(self):

        playlist=Playlist("mp3")
        source_dir =os.path.expanduser(self.path)
        for name in os.listdir(source_dir):
            if name[-4:].lower() != ".mp3":
                continue
            path = os.path.join(source_dir, name)
            audio = EasyID3(path)
            if 'album' not in audio.keys():
                album='No information for the album'
            title=audio['title'][0]
            artist=audio['artist'][0]
            secs=int(MP3(path).info.length)
            duration=str(datetime.timedelta(seconds=secs))
            s=Song(title,artist,album,duration)
            playlist.add_song(s)
        return playlist


def main():
    crawler = MusicCrawler("/home/helious/week02/week05/music")
    playlist = crawler.generate_playlist()
    playlist.pprint_playlist()

if __name__ == '__main__':
    main()