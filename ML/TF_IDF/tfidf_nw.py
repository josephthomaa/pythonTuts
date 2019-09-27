from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np  
import math
import re

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
  "doc2": questions2,
  "doc3":questions3, 
}

Results = pd.DataFrame({'Word': [],'Doc Name': [],"TF value":[],
                    "IDF value":[],"Profile Score":[]}) 
vectorizer = TfidfVectorizer()
cv1 = CountVectorizer()

def termFrequency(term, doc,no):  
      
    """ 
    Input: term: Term in the Document, doc: Document 
    Return: Normalized tf: Number of times term occurs 
      in document/Total number of terms in the document 
    """
    # Splitting the document into individual terms 
    listToStr = ' '.join([str(elem) for elem in doc])
    listToStr = listToStr.replace(',', '') 
    listToStr = re.sub(r'[^\w\s\d]','',listToStr)
    normalizeTermFreq = listToStr.lower().split() 
  
    # Number of times the term occurs in the document 
    term_in_document = normalizeTermFreq.count(term)  
  
    # Total number of terms in the document 
    len_of_document = float(len(normalizeTermFreq ))  
    print(term , ' count = ', term_in_document)
    # Normalized Term Frequency 
    normalized_tf = no / len_of_document  
  
    return normalized_tf 


def inverseDocumentFrequency(term, allDocs): 
    num_docs_with_given_term = 0
  
    """ 
    Input: term: Term in the Document, 
           allDocs: List of all documents 
    Return: Inverse Document Frequency (idf) for term 
            = Logarithm ((Total Number of Documents) /  
            (Number of documents containing the term)) 
    """
    # Iterate through all the documents 
    for doc in allDocs: 
          
        """ 
        Putting a check if a term appears in a document. 
        If term is present in the document, then  
        increment "num_docs_with_given_term" variable 
        """
        if term.lower() in allDocs[doc].lower().split(): 
            num_docs_with_given_term += 1
  
    if num_docs_with_given_term > 0: 
        # Total number of documents 
        total_num_docs = len(allDocs)  
  
        # Calculating the IDF  
        idf_val = log(float(total_num_docs) / num_docs_with_given_term) 
        return idf_val 
    else: 
        return 0


def doc_val_calc(docs_list,Results):
   for doc_name,doc in docs_list.items():
       _X = vectorizer.fit_transform(doc)
       _feature_words = vectorizer.get_feature_names()
       #print(_feature_words)
       x_traincv = cv1.fit_transform(doc)
       x_traincv_df = pd.DataFrame(x_traincv.toarray(),columns=list(cv1.get_feature_names()))
       for x in range(len(_feature_words)):
           no_t_doc = np.sum(x_traincv_df[_feature_words[x]],axis=0)
           tf_val = termFrequency(_feature_words[x],doc,no_t_doc)
           print('TF of word ', _feature_words[x],' : ',tf_val)

doc_val_calc(docs_list,Results)
#termFrequency('the',questions1)