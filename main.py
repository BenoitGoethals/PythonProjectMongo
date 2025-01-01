# This is a sample Python script.
from dotenv import find_dotenv, load_dotenv
import os
import pprint

from pymongo import MongoClient

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
load_dotenv(find_dotenv())
password = os.getenv("MONGODB_PWD")
connection_string = f"mongodb+srv://benoitgoethals:{password}@cluster0.ds9qs.mongodb.net/"


# Press the green button in the gutter to run the script.
def main():
    try:
        with MongoClient(connection_string) as client:
            db = client.sample_mflix
            col2 = db.movies
            pprint.pprint(col2.count_documents({}))
            pprint.pprint(col2.find_one({"title": "The Dark Knight Rises"}))
            id=col2.insert_one({"title": "The Dark Knight 2", "year": 2008}).inserted_id
            pprint.pprint(id)
            for r in col2.find({"year": 2008}):
                pprint.pprint(r)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
