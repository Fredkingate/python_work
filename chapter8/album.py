def make_album(artist_name, album_title, number_of_tracks=None):
    """Return a dictionary of information about an album."""
    while True:
        print("\nPlease tell me the name of an artist and an album:")
        print("(enter 'q' at any time to quit)")
        
        artist_name = input("Artist name: ")
        if artist_name == 'q':
            break
        
        album_title = input("Album title: ")
        if album_title == 'q':
            break
    return album
album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('metallica', 'master of puppets', number_of_tracks=8)
print(album)