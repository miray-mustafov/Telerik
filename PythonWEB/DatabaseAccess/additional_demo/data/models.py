from pydantic import BaseModel


class Artist(BaseModel):
    id: int = None or None
    name: str
    artist_type: str
    bio: str or None


class Song(BaseModel):
    id: int = None or None
    title: str
    artist_id: int or None
    album: str or None


class SongView(BaseModel):
    title: str
    album: str


class ArtistView(BaseModel):
    name: str
    artist_type: str
    bio: str or None
    songs: list[SongView] = None or None







