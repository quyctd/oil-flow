from pymongo import MongoClient

# mongodb://admin:123.abc@@ds159400.mlab.com:59400/oildb
client = MongoClient("mongodb://admin:123.Abc%40@ds159400.mlab.com:59400/oildb")

db = client.oildb
cl = db.blog_answer.find()
for col in cl:
    try:
        val = col['refer_link']
    except:
        val= None
    if val == None:
        db.blog_answer.update({'_id': col['_id']}, {
                                '$set': {'refer_link': "https://stackoverflow.com"}})
