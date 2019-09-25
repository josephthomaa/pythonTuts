from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np  
import itertools
weather = [
    'What is todays weather',
    'Tell me todays weather',
    'What is current weather',
    'sing a weather song',
    'play twinkle twinkle ',
    ]
time = [
    'What is todays time',
    'Tell me todays time',
    'What is current time',
    'sing a time weather',
]

docs_list = [weather,time]
no_of_doc = 2

print(sum('weather' in s for s in weather))
print(sum('weather' in s for s in time))

'''def calc_tfid(word):
    #no_t_doc number of times t appears in doc
    no_of_doc = sum(word in s for s in weather)
    no_of_doc2 = sum(word in s for s in time)

    #tot_t_doc total num of appearance of t in all doc
    tot_t_doc = no_of_doc+no_of_doc2
    result_tfid =	{
        "tfid1": no_of_doc/tot_t_doc,
        "tfid2": no_of_doc2/tot_t_doc
    }
    return result_tfid 

print(calc_tfid('weather'))'''

vectorizer = TfidfVectorizer()
cv1 = CountVectorizer()

'''X = vectorizer.fit_transform(weather)
feature_words = vectorizer.get_feature_names()
print(feature_words)'''
#print(X.shape)  
print(docs_list)
def doc_val_calc(docs):
   for doc in itertools.chain.from_iterable(docs_list):
   #for doc in range(len(docs_list)):
       _X = vectorizer.fit_transform(doc)
       _feature_words = vectorizer.get_feature_names()
       print(_feature_words)


doc_val_calc(docs_list)

x_traincv = cv1.fit_transform(weather)
x_traincv_df = pd.DataFrame(x_traincv.toarray(),columns=list(cv1.get_feature_names()))
print(x_traincv_df)
total_terms = np.sum(x_traincv)
print("Total terms = ", np.sum(x_traincv))

print(np.sum(x_traincv_df['current'],axis=0))


def calc_tfid(words):
    for x in range(len(feature_words)):
        no_t_doc = np.sum(x_traincv_df[feature_words[x]],axis=0)
        print('No of ', feature_words[x], ' = ', no_t_doc)
        tfid = no_t_doc/total_terms
        print(" tfid ", tfid)

      
#print(x_traincv_df['current'])
calc_tfid(feature_words)
   
