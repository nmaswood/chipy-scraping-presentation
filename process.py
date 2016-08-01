import json
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter

def get_political_data():

    with open('truth_data.json','r') as infile:
        json_data = json.load(infile)

        return [(x.get('truth'), x.get('statment').strip()) for x in json_data]

def classify(x):

    # ['Pants on Fire!', 'Full Flop', 'Mostly False', 'False']

    return int(x in ['True', 'Mostly True', 'Half-True', 'No Flip'])

def classified_data():

    init_data = get_political_data()
    return [(classify(x[0]),x[1])for x in init_data]
