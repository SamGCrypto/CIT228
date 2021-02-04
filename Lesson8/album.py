def make_album(artist, title):
    album = {artist:title}
    return album

thisDic={}
while True:
    print("Enter in an artist and album.")
    print("When finished press q in artist")
    artist = str(input("Enter artist: "))
    if artist=='q':
        break
    else:
        title = str(input("Enter album: "))
        album=make_album(artist, title)
        thisDic.update(album)
print(thisDic)
