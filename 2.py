class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class MusicPlaylist:
    def __init__(self):
        self.head = None

    def create_playlist(self, songs):
        for title in songs:
            self.insert_song(title)
        print("Playlist created successfully.")

    def insert_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
        print(f"'{title}' added to playlist.")

    def delete_song(self, title):
        temp = self.head
        prev = None

        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"'{title}' removed from playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"'{title}' not found in playlist.")

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        print(" Music Playlist:")
        temp = self.head
        index = 1
        while temp:
            print(f"{index}. {temp.title}")
            temp = temp.next
            index += 1
def main():
    playlist = MusicPlaylist()

    while True:
        print("\n--- Music Playlist Menu ---")
        print("1. Create Playlist")
        print("2. Insert Song")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            songs = input("Enter song titles separated by commas: ").split(',')
            songs = [song.strip() for song in songs]
            playlist.create_playlist(songs)

        elif choice == '2':
            song = input("Enter the title of the song to add: ").strip()
            playlist.insert_song(song)

        elif choice == '3':
            song = input("Enter the title of the song to delete: ").strip()
            playlist.delete_song(song)

        elif choice == '4':
            playlist.display_playlist()

        elif choice == '5':
            print("Exiting Music Playlist. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
