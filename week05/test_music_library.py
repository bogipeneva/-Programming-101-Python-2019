import unittest
from MusicLibrary import *

class TestMusicLibrary(unittest.TestCase):

    def test_song_initial_value(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        assert s.title == "Odin"
        assert s.artist == 'Manowar'
        assert s.album == "The Sons of Odin"
        assert s._length == "3:44"

    def test_song_str_function(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        expected_result = "{Manowar} - {Odin} from {The Sons of Odin} - {3:44}"
        self.assertEqual(str(s), expected_result)

    def test_song_eq_function(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(s == s2, True)

    def test_song_length_function_when_minutes_argument_is_true_then_return_length_in_minutes(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="2:30:44")
        expected_result = 150
        self.assertEqual(s.length(minutes=True), expected_result)

    def test_song_length_function_when_seconds_argument_is_true_then_return_length_in_seconds(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:00")
        expected_result = 5400
        self.assertEqual(s.length(seconds=True), expected_result)

    def test_song_length_function_when_hours_argument_is_true_then_return_length_in_hours(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="2:30:44")
        expected_result = 2
        self.assertEqual(s.length(hours=True), expected_result)

    def test_song_length_function_with_no_arguments_then_return_strig_representation_of_the_length(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="2:30:44")
        expected_result = '2:30:44'
        self.assertEqual(s.length(), expected_result)

    def test_playlist_initial_value(self):
        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        assert code_songs.name == 'Code'
        assert code_songs.repeat == True
        assert code_songs.shuffle == True
        assert code_songs._Playlist__songs == []

    def test_add_song_when_song_is_passed_return_noting_but_save_song_into_dictionary_of_songs_for_that_playlist(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        code_songs.add_song(s)
        expected_result = [s]
        self.assertEqual(code_songs._Playlist__songs, expected_result)

    def test_remove_song_when_song_is_passed_return_noting_but_remove_given_song_from_list_of_songs_for_that_playlist(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        code_songs.add_song(s)
        code_songs.remove_song(s)
        expected_result = []
        self.assertEqual(code_songs._Playlist__songs, expected_result)


    def test_add_songs_when_is_passed_list_of_songs_then_include_them_into_dictionary_with_songs(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s1 = Song(title="O", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odn", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [s, s1, s2]
        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        code_songs.add_songs(songs)
        expected_result = [s,s1,s2]
        self.assertEqual(code_songs._Playlist__songs, expected_result)

    def test_playlist_total_length_metod_that_returns_string_representation_of_the_total_length_of_the_songs_in_the_playlist(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s1 = Song(title="O", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odn", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [s, s1, s2]

        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        code_songs.add_songs(songs)
        expected_result = '0:11:12'
        self.assertEqual(code_songs.total_length(), expected_result)

    def test_count_of_songs_when_name_of_artist_is_passed_then_return_number_of_his_songs_in_playlist(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s1 = Song(title="O", artist="Moly", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odn", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [s, s1, s2]

        code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        code_songs.add_songs(songs)
        expr = 'Manowar'
        expected_result = 2
        self.assertEqual(code_songs.count_of_songs(expr), expected_result)

    def test_next_song_when_shuffle_is_false_and_repeat_is_true_then_play_songs_from_playlist_in_order_and_if_reaches_the_end_start_from_the_beginning(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s1 = Song(title="O", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odn", artist="Rag", album="The Sons", length="3:44")
        songs = [s, s1, s2]

        code_songs = Playlist(name="Code", repeat=True, shuffle=False)
        code_songs.add_songs(songs)
        self.assertEqual(code_songs.next_song(), code_songs._Playlist__songs[0])
        self.assertEqual(code_songs.next_song(), code_songs._Playlist__songs[1])
        self.assertEqual(code_songs.next_song(), code_songs._Playlist__songs[2])
        self.assertEqual(code_songs.next_song(), code_songs._Playlist__songs[0])

    







if __name__ == '__main__':
    unittest.main()
