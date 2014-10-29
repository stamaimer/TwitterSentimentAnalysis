import preprocess
import classifier
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

    #label.label(twitter)

    #classifier.naive_bayes_classifier(twitter, 1)

    #classifier.max_ent_classifier(twitter, 1)

    #classifier.svm_classifier(twitter, 1)

    classifier.scikit_classifier(twitter, 1)

if __name__ == '__main__':

    main()
