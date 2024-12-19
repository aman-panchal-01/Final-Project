from search_manager import SongSearch
from song_search_exception import ArtistNotFoundException , EmptyDataBaseException, InvalidFileFormatException, SongNotFoundException
class MENU:
    def __init__(self):
        self.song = SongSearch()
    
    def user_menu(self):
        print('Welcome to Spotify User Menu !')
        
        while True:
            print('First, load the database.')
            file_name = input('Enter file name: ')
            
            # Loop until a valid file is loaded
            try:
                temp = self.song.load_database(file_name)
                if temp:
                    break  # If the file is successfully loaded, exit the loop
                else:
                    print('Invalid file format. Please try again.')
            except FileNotFoundError as e:
                print(f"File not found: {e}. Please try again.")
            except InvalidFileFormatException as e:
                print(f"Invalid file format: {e}. Please try again.")
        print('Database has been Loaded Successfully.')
        while True:
            print('\t-Press 1 for Search Song by its Name \n\t-Press 2 for Search song by Artist\n\t-Press 3 for Exit')
            choice = input('Enter your choice here : ')
            if choice == '1':
                self.song.search_by_title()
            elif choice == '2':
                self.song.search_by_artist()
            elif choice == '3':
                print('Successfully Exit from Program! ')
                break
            else:
                print('invalid choice! ')
                
if __name__ == "__main__":
    menu = MENU()
    menu.user_menu()
    print('Thanks for Using Spotify.')