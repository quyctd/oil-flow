from pymongo import MongoClient
from django.template.defaultfilters import slugify

# mongodb://admin:123.abc@@ds159400.mlab.com:59400/oildb
client = MongoClient("mongodb://admin:123.Abc%40@ds159400.mlab.com:59400/oildb")

db = client.oildb
cl = db.blog_question.find()
for col in cl:
    slug = slugify(col['title'])
    db.blog_question.update({'_id': col['_id']},{'$set': {'slug': slug}})
