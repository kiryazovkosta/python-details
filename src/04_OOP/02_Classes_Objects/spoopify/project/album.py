from project.song import Song

class Album:
    def __init__(self, name:str, *songs, published: bool = False):
        self.name = name
        self.songs = []
        self.published = published
        [self.songs.append(song) for song in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = next((s for s in self.songs if s.name == song_name), None)
        if song:
            if self.published:
                return "Cannot remove songs. Album is published."
            else:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        else:
            return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {song.get_info()}") for song in self.songs]
        return '\n'.join(result)




