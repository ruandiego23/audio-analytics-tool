# analysis.py
from musiclib.models import Track, Playlist

# 1. Create a few tracks (Notice I'm creating them out of order!)
t1 = Track(artist="Zelda Soundtrack", title="Song of Storms", duration_seconds=180, genre="OST")
t2 = Track(artist="Daft Punk", title="One More Time", duration_seconds=320, genre="Electronic")
t3 = Track(artist="Abba", title="Dancing Queen", duration_seconds=230, genre="Pop")

# 2. Create a Playlist
my_playlist = Playlist(name="Coding Vibes")

# 3. Add tracks
print("--- Adding Tracks ---")
my_playlist.add_track(t1)
my_playlist.add_track(t2)
my_playlist.add_track(t3)

print(f"Created: {my_playlist}")

# 4. The Magic Test: Sorting
# Because we used order=True, we can sort the list directly!
print("\n--- Testing Magic Sort (By Artist) ---")
sorted_tracks = sorted(my_playlist.tracks)

for track in sorted_tracks:
    print(track)
