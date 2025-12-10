from dataclasses import dataclass, field


@dataclass(order=True)
class Track:
    artist: str
    title: str
    duration_seconds: int = field(compare=False)
    genre: str = field(default="Unknown", compare=False)

def __str__(self) -> str:
    return f"{self.artist} - {self.title} ({self.duration_seconds}s)"


@dataclass
class Playlist:
    name: str
    # This is the "magic" line:
    tracks: list[Track] = field(default_factory=list)

    def add_track(self, track: Track):
        """Helper to add a track to the list."""
        self.tracks.append(track)

    def __str__(self) -> str:
        return f"Playlist: {self.name} ({len(self.tracks)} tracks)"
