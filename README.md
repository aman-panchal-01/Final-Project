# Python-Final-Project
# Spotify Song Management System

## Overview

This is a Python-based song management system that allows users to load a song database, search for songs, and modify or delete songs from the database. The system is divided into multiple modules to manage different functionalities such as loading the database, searching songs, and handling exceptions.

### Features

1. **Load Database**: Load a '.txt' file that contains song data into the system.
2. **View Songs**: View the songs stored in the database.
3. **Delete Song**: Delete a song based on its title and artist.
4. **Modify Song**: Modify song details (album, genre, duration).
5. **Search Songs**: Search for songs by their title or artist.
6. **Handle Exceptions**: Properly handle various exceptions such as missing files, invalid formats, and missing song/artist.

---

## Modules

### 1. **song_manager.py**

This module handles the song database operations, such as loading the data from a file, saving the updated data, and performing actions like viewing, deleting, and modifying songs.

#### Methods:
- **load_database(file_name)**: Loads a song database from a specified file and parses the data into a dictionary.
- **song_viewer()**: Displays all songs in the database.
- **delete_song()**: Deletes a song from the database based on the artist and title.
- **modify_song()**: Allows the modification of song details (album, genre, duration).
- **save_database()**: Saves the current song database back to the file.
- **get_artist_name(artist_name)**: Finds the artist in the database.

### 2. **search_manager.py**

This module allows users to search for songs by title or artist.

#### Methods:
- **load_database(file_name)**: Loads the song database from a txt file.
- **search_by_title()**: Searches for songs by their title.
- **search_by_artist()**: Searches for songs by artist name.
- **get_artist_name(artist_name)**: Returns the artist name if found in the database.

### 3. **user_menu.py**

This module defines the user interface, allowing users to load the song database and choose various operations such as searching for songs or exiting the application.

#### Methods:
- **user_menu()**: Displays the main menu to the user, where they can choose options to search for songs, load the database, or exit the program.

### 4. **song_exception.py**

This module defines custom exceptions used in the project to handle specific error conditions, such as missing files, invalid formats, or missing song/artist.

#### Exceptions:
- **ArtistNotFoundException**: Raised when an artist is not found in the database.
- **EmptyDataBaseException**: Raised when the database is empty.
- **SongNotFoundException**: Raised when a song is not found in the database.
- **InvalidFileFormatException**: Raised when the format of the input file is invalid.

## Usage

After running the program, the user will be presented with a menu to interact with the song database. The options are as follows:

1. **Load Database**: Prompt to enter the file name of the song database. The file should contain song data in the format specified above.
2. **Search Songs**:
   - **By Title**: Allows the user to search for a song by its title.
   - **By Artist**: Allows the user to search for songs by the artist's name.
3. **Delete Song**: Prompts the user to enter an artist name and song title to delete a specific song from the database.
4. **Modify Song**: Allows the user to modify song details like album, genre, and duration.
5. **Exit**: Exits the program.

---

## Exception Handling

The program includes the following exception handling:

- **FileNotFoundError**: Raised when the specified file cannot be found.
- **InvalidFileFormatException**: Raised when the txt file format is incorrect.
- **EmptyDataBaseException**: Raised when the database is empty.
- **ArtistNotFoundException**: Raised when the specified artist is not found in the database.
- **SongNotFoundException**: Raised when the specified song is not found in the database.

---

## Example Format for File

The song database should be in this format, with each line containing the following columns:
- Song Title
- Artist Name
- Album
- Genre
- Duration (in minutes and seconds)

Example:

```txt
"Shape of You","Ed Sheeran","Divide","Pop","3:53"
"Blinding Lights","The Weeknd","After Hours","Pop","3:20"
"Levitating","Dua Lipa","Future Nostalgia","Pop","3:23"
```

---




**Thank you for using the Spotify Song Management System!**
