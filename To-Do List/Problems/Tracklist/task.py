def tracklist(**kwargs):
    for musician in kwargs:
        print(musician)
        for album in kwargs[musician]:
            print(f"ALBUM: {album} TRACK: {kwargs[musician][album]}")


# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
