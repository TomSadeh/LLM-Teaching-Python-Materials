# Exercise 8: Playlist Shuffler

import random


def shuffle_playlist(songs):
    # ✏️ YOUR CODE HERE ✏️
    # Shuffle the songs list to put them in random order
    # Hint: use random.shuffle(list) - this changes the list directly
    pass


def show_playlist(songs, title):
    """Display the playlist with a title"""
    print("\n" + title)
    print("-" * len(title))
    for i in range(len(songs)):
        print(str(i + 1) + ". " + songs[i])


def main():
    # Start with a sample playlist
    playlist = [
        "Happy - Pharrell",
        "Shake It Off - Taylor Swift",
        "Uptown Funk - Bruno Mars",
        "Can't Stop the Feeling - Justin Timberlake",
        "Old Town Road - Lil Nas X"
    ]

    show_playlist(playlist, "Original Playlist")

    input("\nPress Enter to shuffle...")

    shuffle_playlist(playlist)

    show_playlist(playlist, "Shuffled Playlist")


main()
