from song_exception import ArtistNotFoundException , EmptyDataBaseException, InvalidFileFormatException, SongNotFoundException
class SongDataBase:
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
        except FileNotFoundError as e:
            print(e)
        except InvalidFileFormatException as e:
            print(e)
        # print(self.database)
        
    def song_viewer(self):
        try:
            if not self.database:
                raise EmptyDataBaseException()
            print('|',f"{'No':<10}{'Song Title':<45}{'Artist':<45}{'Genre':<30}",'|')
            print("-"*140)
            sr = 1
            for artist, songs in self.database.items():
                for title,info in songs.items():
                    print('|',f"{sr:<10}{title:<45}{artist:<45}{info['genre']:<30}",'|')
                    sr+=1
        except EmptyDataBaseException as e:
            print(e)
        except FileNotFoundError as e:
            print(e)

                
                
    def delete_song(self):
        try:
            if self.database:
                print("To Delete a Song please enter Song Artist and Song Name ")
                artist = input('Enter the artist name : ')
                valid_artist = self.get_artist_name(artist)
                if valid_artist!= False:
                    print('Artist found')
                    print('Here are the all song of that artist')
                    j = 1
                    for song in self.database[valid_artist]:
                        print(j,'-',song)
                        j+=1
                    title = input('Enter snog title : ').strip().lower()
                    for database_title in list(self.database[valid_artist]):
                        if database_title.lower() == title.lower():
                            del self.database[valid_artist][database_title]
                            print(f'{title} by {valid_artist} has been deleted from database.')
                            print('You can check by Press 2 !')
                            return
                        
                    raise SongNotFoundException()
                else:
                    raise ArtistNotFoundException()
            else:
                raise EmptyDataBaseException()
        except EmptyDataBaseException as e:
            print(e)
        except SongNotFoundException as e:
            print(e)
        except ArtistNotFoundException as e:
            print(e)
        
    def modify_song(self):
        try:
            if not self.database:
                raise EmptyDataBaseException()
            print('To Modify a song please fill the details correctly')
            artist = input('Enter the artist name for modifying : ').strip()
            valid_artist = self.get_artist_name(artist)
            if valid_artist != False:
                print('Artist Found ! \nWhich song you want to Modify ?')
                j = 1
                for song in self.database[valid_artist]:
                    print(j,'-',song)
                    j+=1
                title = input('Enter Song Title: ').strip().lower()
                for database_title , song_info in self.database[valid_artist].items():
                    if database_title.lower() == title:
                        print('Song Found !!')
                        album = song_info['album']
                        genre = song_info['genre']
                        duration = song_info['duration']
                        new_album = input('Enter new album or press enter to keep old one : ') or album
                        new_genre = input('Enter new genre or press enter to keep old one : ') or genre
                        new_duration = input('Enter new duration (in Min|Sec foramt) or keep old one:  ') or duration
                        song_info['album'] = new_album
                        song_info['genre'] = new_genre
                        song_info['duration'] = new_duration
                        print('Song Detail Updated Successfully.')
                        print("\nSong details updated successfully!")
                        print("Updated Song Information:")
                        print(f"Title: {database_title}")
                        print(f"Artist: {valid_artist}")
                        print(f"Album: {song_info['album']}")
                        print(f"Genre: {song_info['genre']}")
                        print(f"Duration: {song_info['duration']}")
                        return
                        
                    
                raise SongNotFoundException()
                        
            else:
                 raise ArtistNotFoundException()          
            
        except EmptyDataBaseException as e:
            print(e)
        except ArtistNotFoundException as e:
            print(e)
        except SongNotFoundException as e:
            print(e)
        except Exception as e:
            print('An Unknow Error Occured !!')
        
    
    def save_database(self):
        try:
            with open(self.file_name , 'w') as f:
                for artist , song in self.database.items():
                    for title,info in song.items():
                        f.write(f'"{title}","{artist}","{info["album"]}","{info["genre"]}","{info["duration"]}"\n')
                    
            print('The new updated data has been saved to the database.')
        except Exception as e:
            print('An Unknown Error Occured While Saving the File Please Try Agaain !')
    def get_artist_name(self, artist_name):
        try:
            for artist in self.database:
                if artist.lower() == artist_name.lower():
                    return artist
            raise ArtistNotFoundException()
        except ArtistNotFoundException as e:
            print(e)
            return False