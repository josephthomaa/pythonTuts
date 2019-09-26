from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np  
import math


time = [
    'What is todays time',
    'Tell me todays time',
    'What is current time',
    'sing a time weather python',
]

no_of_d = 2
wiki = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/wikepedia.csv')
weather = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/weather.csv')
quotes = pd.read_csv('/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/quotes.csv')
#test = test.dropna(axis=0)

questions1 = wiki['Questions']
questions2 = time
questions3 = quotes['Questions']

questions1 = [element.lower() for element in questions1]
questions2 = [element.lower() for element in questions2]
questions3 = [element.lower() for element in questions3]
#print(questions1)
docs_list =	{
  "doc1": questions1,
  "doc2": questions2,
  "doc3": questions3,
}

Results = pd.DataFrame({'Word': [],'Doc Name': [],"TF value":[],
                    "IDF value":[],"Profile Score":[]}) 

vectorizer = TfidfVectorizer()
cv1 = CountVectorizer()

 
def calc_idf(docs,word):
    count = 0
    for doc in docs_list.values():
        doc_set = set(doc) 
        #print('count of ',word ,' = ',sum(word in s for s in doc))
        if(sum(word in s for s in doc)>0):
            count=count+1
    print('count of docs with ',word ,' = ',count)
    return count    


def calc_tf_idf(words,x_traincv_df,total_terms,doc_name,Results):
    for x in range(len(words)):
        no_t_doc = np.sum(x_traincv_df[words[x]],axis=0)
        #print('No of ', words[x], ' = ', no_t_doc)
        tfid = no_t_doc/total_terms
        print(" tfid ", tfid)
        no_of_dt = calc_idf(docs_list,words[x])

        #idf = log(Total Number Of Documents / Number Of Documents with term Computer in it)
        idf = math.log(3/no_of_dt)
        print('idf = ',idf)

        tf_idf = tfid*idf
        res = pd.DataFrame({"Word":[words[x]],"Doc Name": [doc_name],"TF value":[tfid],"IDF value":[idf],"Profile Score":[tf_idf]})
        Results = Results.append(res)
    return Results    
        

def doc_val_calc(docs_list,Results):
   for doc_name,doc in docs_list.items():
       _X = vectorizer.fit_transform(doc)
       _feature_words = vectorizer.get_feature_names()
       #print(_feature_words)
       print('doc = ' ,doc) 
       x_traincv = cv1.fit_transform(doc)
       x_traincv_df = pd.DataFrame(x_traincv.toarray(),columns=list(cv1.get_feature_names()))
       print(x_traincv_df)
       total_terms = np.sum(x_traincv)
       print("Total terms = ", np.sum(x_traincv))

       #print(np.sum(x_traincv_df['current'],axis=0))
       Results = calc_tf_idf(_feature_words,x_traincv_df,total_terms,doc_name,Results)
   return Results    
       


out_result = doc_val_calc(docs_list,Results)
export_csv = out_result.to_csv (r"/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/export_dataframe.csv", index = None, header=True) 
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(out_result)
#print(out_result)




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

'''X = vectorizer.fit_transform(weather)
feature_words = vectorizer.get_feature_names()
print(feature_words)'''
#print(X.shape) 



'''x_traincv = cv1.fit_transform(weather)
x_traincv_df = pd.DataFrame(x_traincv.toarray(),columns=list(cv1.get_feature_names()))
print(x_traincv_df)
total_terms = np.sum(x_traincv)
print("Total terms = ", np.sum(x_traincv))

print(np.sum(x_traincv_df['current'],axis=0))'''




      
#print(x_traincv_df['current'])

   
