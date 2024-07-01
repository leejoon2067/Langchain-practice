from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip_Hop'

Bands = [
    {'id' : 1, 'name' : 'The Kinks', 'genre' : 'Rock'},
    {'id' : 2, 'name' : 'Aphex Twin', 'genre' : 'Electronic'},
    {'id' : 3, 'name' : 'Black Sabbath', 'genre' : 'Metal'},
    {'id' : 4, 'name' : 'Wu-Tang Clan', 'genre' : 'Hip_Hop'},
]

@app.get('/bands') # decorator (get, put, post, delete 등 함수 활용)
async def bands() -> list[dict]:
    return Bands

@app.get('/bands/{band_id}')
async def band(band_id : int) -> dict:
    band = next((b for b in Bands if b['id'] == band_id), None)
    if band is None: 
        # status code 404
        raise HTTPException(status_code = 404, detail = 'Band not found')
    else:
        return band
    
@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre : GenreURLChoices) -> list[dict]:
    return [
        b for b in Bands if b['genre'] == genre.value
    ]