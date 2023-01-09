# ----------------------------------
# ----- Path parameters ------------
# ----------------------------------


from fastapi import FastAPI
from pymongo import MongoClient
from pathlib import Path

mongo_uri = "mongodb://localhost"
client = MongoClient(mongo_uri)

db = client['sample_linio']
app = FastAPI()


@app.get("/top10-products")
async def products():
    sales_normalize = db['sales_normalize']
    out = sales_normalize.aggregate([{
        "$group": {
            "_id": "$items.product_id",
            "Total": {
                "$sum": "$items.quantity"
            }
        }
    }, {
        "$sort": {
            "Total": -1
        }
    }, {
        "$limit": 10
    }])
    return list(out)


# Here the age is variable
# so we can pass the age, but this must an integer, if we pass a letter or float this return error
@app.get("/products/ge-{age}")
async def users_ge(age: int):
    users = db['users']
    out = users.find({
        "ages": {
            "$gte": age
        }
    }, {
        "_id": 0
    }).limit(10)

    return list(out)


# Here we the licence must match at pattern 4 digits + - + 4 letters
bought = ['1055-ADQW', '6270-QPLK', '5065-ALOP']


@app.get("/licences/{licence}")
async def test_licence(licence: str = Path(regex=r'(\d{4}-[A-Z]{4})$')):
    if licence in bought:
        return 'Your licence is actived'
    else:
        return 'Your licence is not actived'


# Other options for Path apart of regex
# gt: Greater than
# ge: Greater than or equal to
# lt: Less than
# le: Less than or equal to

