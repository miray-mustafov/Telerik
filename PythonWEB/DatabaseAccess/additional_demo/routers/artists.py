from fastapi import APIRouter, Response
from services import artists_services
from data.models import Artist

artists_router = APIRouter(prefix='/artists')


@artists_router.get('/')
def get_artists():
    result = artists_services.get_all()
    return result


@artists_router.get('/{id}')
def get_artist_by_id(id: int):
    result = artists_services.get_by_id(id)

    return result


@artists_router.put('/{id}')
def update_artist(id: int, artist: Artist):
    existing_artist = artists_services.exits(id)

    if not existing_artist:
        return Response(status_code=404)
    else:
        return artists_services.update(existing_artist, artist)


@artists_router.post('/')
def create_artist(artist: Artist):
    if not artist:
        return Response(status_code=404)
    else:
        return artists_services.create(artist)


@artists_router.delete('/{id}')
def delete_artist(id: int):
    existing_artist = artists_services.exits(id)

    if not existing_artist:
        return Response(status_code=404)
    else:
        return artists_services.delete(existing_artist)