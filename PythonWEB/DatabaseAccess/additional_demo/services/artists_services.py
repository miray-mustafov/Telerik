from data.database import read_query, update_query, insert_query
from data.models import Artist, ArtistView, SongView


def get_all():
    data = read_query('select id, name, artist_type, bio from artists')

    return (Artist(id=id, name=name, artist_type=artist_type, bio=bio) for id, name, artist_type, bio in data)


def get_by_id(id):
    songs = read_query('select title, album from songs where artist_id = ?', (id,))
    artist = read_query('select name, artist_type, bio from artists where id = ?', (id,))
    name, artist_type, bio = artist[0]
    songs_list = [SongView(title=title, album=album) for title, album in songs]

    return ArtistView(name=name, artist_type=artist_type, bio=bio, songs=songs_list)


def update(existing_artist: Artist, artist: Artist):
    update_query('update artists set name = ?, artist_type = ?, bio = ? where id = ?', (artist.name, artist.artist_type,
                                                                                        artist.bio, existing_artist.id))

    return f'Artist with id: {existing_artist.id} was successfully updated!'


def exits(id: int):
    existing_artist = read_query('select id, name, artist_type, bio from artists where id = ?', (id,))
    return next((Artist(id=id, name=name, artist_type=artist_type, bio=bio) for id, name, artist_type, bio in existing_artist), None)


def create(artist: Artist):
    generated_id = insert_query('insert into artists (name, artist_type, bio) values (?, ?, ?)',
                                (artist.name, artist.artist_type, artist.bio))

    # artist.id = generated_id

    return f'Artist {artist.name} was successfully created!!'


def delete(existing_artist: Artist):
    update_query('delete from artists where id = ?', (existing_artist.id,))

    return f'Artist {existing_artist.name} was successfully deleted!'

