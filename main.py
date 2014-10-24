import preprocess
import pymongo
import ngrams
import label

def get_db():

    mongo_client = pymongo.MongoClient('127.0.0.1', 27017)

    twitter = mongo_client.twitter

    return twitter

def main():

    twitter = get_db()

    #preprocess.remove(twitter)

    #preprocess.preprocess(twitter)

    #ngrams.get_unigram(twitter)

    #ngrams.get_bigram(twitter)

    #ngrams.get_trigram(twitter)

    label.label(twitter)

if __name__ == '__main__':

    main()
