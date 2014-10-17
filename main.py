import preprocess
import pymongo

def get_db():

    mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

    twitter = mongo_client.twitter

    return twitter

def main():

    twitter = get_db()

    preprocess.remove(twitter)

    preprocess.preprocess(twitter)

if __name__ == '__main__':

    main()
