import divide
import progressbar

def label(twitter):

    preprocessed = twitter.preprocessed

    count = preprocessed.count()

    preprocessed = preprocessed.find({}, {'text':1, '_id':0})

    print "label tweets"

    bar = progressbar.ProgressBar(maxval = count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    i = 0

    for tweet in preprocessed:

        text = tweet['text']

        twitter.labeled.insert({'text':text, 'label':divide.DivideEmotion(text)})

        bar.update(i + 1)

        i = i + 1

    bar.finish()


