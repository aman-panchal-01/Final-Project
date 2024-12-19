class ArtistNotFoundException (Exception):
    def __init__(self):
        super().__init__("Artist Not Found !")
        
class EmptyDataBaseException(Exception):
    def __init__(self):
        super().__init__("Provided Database is Empty !")
        
class SongNotFoundException(Exception):
    def __init__(self):
        super().__init__("Current Song is not Found in Exception !")
        
        
class InvalidFileFormatException(Exception):
    def __init__(self):
        super().__init__("Invalid Format of Provided File !")
