from enum import Enum
import aiofiles
import uuid

from fastapi import FastAPI, UploadFile

class Method(str, Enum):
    SPECIES = 'species'
    DISEASE = 'disease'

app = FastAPI()


@app.post('/detect/{method}')
async def detect(method: Method, img: UploadFile):
    filepath = f'./images/{uuid.uuid4()}.jpeg'
    async with aiofiles.open(filepath, 'wb') as out_file:
        data = await img.read()
        await out_file.write(data)

    if method is Method.DISEASE:
        return {'diagnosis': 'trachobobers', 'recommendations': '123'}
    elif method is Method.SPECIES:
        return {'russian_title': 'aboba', 'latin_title': 'bebra'}

    return None