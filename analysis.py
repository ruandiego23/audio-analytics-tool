# analysis.py
from musiclib.models import Track, Playlist
import pandas as pd

# === PHASE 1: CREATE DATA ===

# 1. Create a few tracks (Notice I'm creating them out of order!)
t1 = Track(artist="Zelda Soundtrack", title="Song of Storms", duration_seconds=180, genre="OST")
t2 = Track(artist="Daft Punk", title="One More Time", duration_seconds=320, genre="Electronic")
t3 = Track(artist="Abba", title="Dancing Queen", duration_seconds=230, genre="Pop")
t4 = Track(artist="Mozart", title="Symphony No. 40", duration_seconds=1500, genre="Classical")

# 2. Create a Playlist
my_playlist = Playlist(name="Coding Vibes")

# 3. Add tracks to the playlist (CRITICAL STEP!)
my_playlist.add_track(t1)
my_playlist.add_track(t2)
my_playlist.add_track(t3)
my_playlist.add_track(t4)

print(f"✅ Successfully created: {my_playlist}")

# === PHASE 2: DATA ANALYSIS ===
# 1. Convert our Playlist object into a list of dictionaries
# Pandas loves dictionaries. We can iterate over our tracks to make this easy.
data = [
    {"Artist": t.artist, "Title": t.title, "Seconds": t.duration_seconds, "Genre": t.genre}
    for t in my_playlist.tracks
]

# 2. Load it into a DataFrame (Excel on steroids)
df = pd.DataFrame(data)

print("\n--- 📊 Your Music Library ---")
print(df)

print("\n--- 🧠 Quick Stats ---")
# Calculate total duration in minutes
total_mins = df["Seconds"].sum() / 60
print(f"Total Listening Time: {total_mins:.2f} minutes")

# Find the shortest song
shortest = df.loc[df["Seconds"].idxmin()]
print(f"Shortest Banger: {shortest['Title']} by {shortest['Artist']}")
