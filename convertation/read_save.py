from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
import io

def read(collection):
    client = MongoClient()
    db = client["picture_mongo"]
    images = db[collection]
    image = images.find()
    k = []
    t = []
    for i in image:
        k.append(Image.open(io.BytesIO(i['img'])))
        t.append(i['text'])
    return [k, t, db.list_collection_names()]


def save(collection):
    client = MongoClient()
    db = client['picture_mongo']
    images = db[collection]

    im = Image.open("hist/Old/8.jpg")

    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')
    txt = "Татары держали в страхе всех в том числе и Русское княжество."
    image = {
        'img': image_bytes.getvalue(),
        'text': txt
    }

    image_id = images.insert_one(image).inserted_id

# save('old')