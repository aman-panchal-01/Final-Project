from song_exception import ArtistNotFoundException , EmptyDataBaseException, InvalidFileFormatException, SongNotFoundException   
from song_manager import SongDataBase           
class MENU:
    def __init__(self):
        self.songdb = SongDataBase()
    
    def user_menu(self):
        print('Welcome to Devlopers Menu!')
        while True:
            print(' Press 1 for load Database \n Press 2 for View Songs Database \n Press 3 for Delete a Song \n Press 4 for Modify a Song \n Press 5 for Exit')
            choice = input("Enter your Choice here : ")
            if choice == '1':
                try:
                    file_name = input("Enter a Valid File Name: ")
                    self.songdb.load_database(file_name)
                    if not file_name:
                        raise EmptyDataBaseException()
                except EmptyDataBaseException as e:
                    print(e)
            elif choice == '2':
                self.songdb.song_viewer()
            elif choice == '3':
                self.songdb.delete_song()
            elif choice == '4':
                print('press 4')
                self.songdb.modify_song()
            elif choice == '5':
                print('You have exited from Program')
                break
            else:
                print("Invalid choice")
            print('\n')
        self.songdb.save_database()
        
if __name__ == "__main__":
    menu = MENU()
    menu.user_menu()
    print('Thanks for Using Spotify.')