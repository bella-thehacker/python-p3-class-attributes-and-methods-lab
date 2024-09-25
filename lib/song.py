
class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count and update genres, artists, and their counts
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

# Accessing attributes
print(ninety_nine_problems.name)   # Output: "99 Problems"
print(ninety_nine_problems.artist) # Output: "Jay-Z"
print(ninety_nine_problems.genre)  # Output: "Rap"

# Checking class attributes
print(Song.count)            # Output: 1
print(Song.genres)           # Output: ['Rap']
print(Song.artists)          # Output: ['Jay-Z']
print(Song.genre_count)      # Output: {'Rap': 1}
print(Song.artist_count)     # Output: {'Jay-Z': 1}
