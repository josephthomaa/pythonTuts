from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np  
import math


wiki = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/wikepedia.csv')
weather = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/weather.csv')
quotes = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/quotes.csv')

questions1 = wiki['Questions']
questions2 = weather['Questions']
questions3 = quotes['Questions']

questions1 = [element.lower() for element in questions1]
questions2 = [element.lower() for element in questions2]
questions3 = [element.lower() for element in questions3]
#print(questions2)
docs = [questions1,questions2,questions3]
docs_list =	{
  "doc1": questions1,
 
}

cv=CountVectorizer()
 
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(questions1)
print(word_count_vector.shape)
 
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

# print idf values
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
 
# sort ascending
print(df_idf.sort_values(by=['idf_weights']))

# count matrix
count_vector=cv.transform(questions1)
 
# tf-idf scores
tf_idf_vector=tfidf_transformer.transform(count_vector)

feature_names = cv.get_feature_names()
 
#get tfidf vector for first document
first_document_vector=tf_idf_vector[0]
 
#print the scores
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.sort_values(by=["tfidf"],ascending=False))
#print(df.sort_values(by=["tfidf"],ascending=False))
    
