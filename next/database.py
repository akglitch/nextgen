from pymongo import MongoClient


client = MongoClient("mongodb+srv://kaytee:kayteezy@cluster0.mzj7oqr.mongodb.net/?retryWrites=true&w=majority")


db = client.student_application

collection_name = db["student_app"]




