from song_search_exception import ArtistNotFoundException , EmptyDataBaseException, InvalidFileFormatException, SongNotFoundException
class SongSearch:
    def __init__(self):
        self.database = {}
        self.file_name = None

    def load_database(self,file_name):
        # Creating a Temprory Database for geeting the file infromation
        temp_data = {}
        self.file_name = file_name
        try:
            with open(self.file_name,'r') as f:
                temp_data =f.read()
                temp_data = temp_data.strip().split('\n')
                 
            for i in temp_data:
                rows = [rows.strip('"') for rows in i.split(',')]
                if len(rows) <5:
                    raise InvalidFileFormatException
                title = rows[0]
                artist = rows[1]
                album = rows[2]
                genre = rows[3]
                duration = rows[4]
                
                if artist not in self.database:
                    self.database[artist] = {}
                      
                self.database[artist][title] = {
                    "album":album,
                    "genre":genre,
                    "duration":duration,
                }
            return True
        except FileNotFoundError as e:
            print(e)
        except InvalidFileFormatException as e:
            print(e)
            
    def search_by_title(self):
        try:
            if not self.database:
                raise EmptyDataBaseException()
            flag = False
            print('Search song by Song Name')
            title = input('Enter title of the song : ').lower()
            for artist , song in self.database.items():
                for song_title , info  in song.items():
                    if song_title.lower() == title:
                        print(f"Song Found: {song_title}")
                        print(f"Artist: {artist}")
                        print(f"Album: {info['album']}")
                        print(f"Genre: {info['genre']}")
                        print(f"Duration: {info['duration']}\n")
                        flag = True
            if not flag:
                raise SongNotFoundException()
        except SongNotFoundException as e:
            print(e)
        except EmptyDataBaseException as e:
            print(e)
    
    def search_by_artist(self):
            try:
                if not self.database:
                    raise EmptyDataBaseException()
                print('Search Songs by Artist Name.')
                artist = input('Enter Artist Name: ').lower()
                valid_artist = self.get_artist_name(artist)
                if valid_artist != False:
                    print(f'The Artist "{valid_artist}" found ! ')
                    i=1
                    for songs,song_info in self.database[valid_artist].items():
                        print(f'{i}-{songs}')
                        print(f'\tAlbum: {song_info['album']}')
                        print(f'\tGenre: {song_info['genre']}')
                        print(f'\tDuration: {song_info['duration']}')
                        i+=1
                        
                else:
                    raise ArtistNotFoundException()
                
            except EmptyDataBaseException as e:
                print(e)
            except ArtistNotFoundException as e:
                print(e)
                
    def get_artist_name(self, artist_name):
        try:
            for artist in self.database:
                if artist.lower() == artist_name.lower():
                    return artist
            raise ArtistNotFoundException()
        except ArtistNotFoundException as e:
            print(e)
            return False
        
            
        