from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np  
import math

xls = pd.ExcelFile('ML/TF_IDF/data/questions.xlsx')
docs_list = {}
for sheet in xls.sheet_names:
    df1 = pd.read_excel(xls, sheet)
    df1 =  df1['Questions']
    docs_list[sheet] = [element.lower() for element in df1]
#debug

#import pdb;pdb.set_trace()
#print(xls.sheet_names)

Results = pd.DataFrame({'Word': [],'Doc Name': [],"TF value":[],
                    "IDF value":[],"TF_IDF Score":[]}) 

#define tfid vectorizer , removing words with length less than 3
vectorizer = TfidfVectorizer(
    stop_words='english',
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'\w{2,}',  #vectorize 2-character words or more
    ngram_range=(1, 1),
    max_features=30000)
cv1 = CountVectorizer()

 
def calc_idf(docs,word):
    count = 0
    for doc in docs_list.values():
        doc_set = set(doc) 
        #print('count of ',word ,' = ',sum(word in s for s in doc))
        if(sum(word in s for s in doc)>0):
            count=count+1
    #print('count of docs with ',word ,' = ',count)
    return count    


def calc_tf_idf(words,x_traincv_df,total_terms,doc_name,Results):
    for x in range(len(words)):
        #no of times term appear in given doc
        no_t_doc = np.sum(x_traincv_df[words[x]],axis=0)
        #print('No of ', words[x], ' = ', no_t_doc)
        tf = no_t_doc/total_terms
        #print(" tfid ", tfid)
        no_of_dt = calc_idf(docs_list,words[x])

        #idf = log(Total Number Of Documents / Number Of Documents with term Computer in it)
        idf = math.log(7/no_of_dt)
        #print('idf = ',idf)

        tf_idf = tf*idf
        res = pd.DataFrame({"Word":[words[x]],"Doc Name": [doc_name],"TF value":[tf],"IDF value":[idf],"TF_IDF Score":[tf_idf]})
        Results = Results.append(res)  
    return Results    
        

def doc_val_calc(docs_list,Results):
   for doc_name,doc in docs_list.items():
       _X = vectorizer.fit_transform(doc)
       _feature_words = vectorizer.get_feature_names()
       #print(_feature_words)
       #print('doc = ' ,doc) 
       x_traincv = cv1.fit_transform(doc)
       x_traincv_df = pd.DataFrame(x_traincv.toarray(),columns=list(cv1.get_feature_names()))
       #print(x_traincv_df)
       total_terms = np.sum(x_traincv)
       #print("Total terms = ", np.sum(x_traincv))

       #print(np.sum(x_traincv_df['current'],axis=0))
       Results = calc_tf_idf(_feature_words,x_traincv_df,total_terms,doc_name,Results)
   return Results    
       


out_result = doc_val_calc(docs_list,Results)
out_result = out_result.sort_values('TF_IDF Score',ascending=False)
top_result = out_result
top_result['Word'].sort_values().unique()
top_result = top_result.head(50)
top_words = top_result['Word'].tolist()
export_csv = top_result.to_csv (r"/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/doc_profile.csv", index = None, header=True) 
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(top_result)
#print(out_result)
print("Top 50 Words ",top_words)

#Term Document Matrix
TD_Matrix = pd.DataFrame({'Word': [],'Wikipedia': [],"News":[],
                    "Weather":[],"Random famous quotes":[],"Synonym":[],"Jokes":[],"Global Time":[]})

# better logic if possible 
for _word in top_words:
    if((out_result.loc[out_result['Word'] == _word]).empty):
        res = pd.DataFrame({'Word': [_word],'Wikipedia': [0],"News":[0],
                    "Weather":[0],"Random famous quotes":[0],"Synonym":[0],"Jokes":[0],"Global Time":[0]})
        TD_Matrix = TD_Matrix.append(res)    
    else:
        word_result = out_result.loc[out_result['Word'] == _word]
        #Wike = word_result['Doc Name'] if word_result['Doc Name'] == 'Wikipedia' else 0 
        #print(word_result['Doc Name'])
        wiki=news=weather=rfm=syn=jokes=gt = 0
        for index, row in word_result.iterrows():
            print(row['Word'],row['Doc Name'],row['TF_IDF Score'])
            wiki = wiki+row['TF_IDF Score'] if (row['Doc Name'] == 'Wikipedia') else wiki
            news = news+row['TF_IDF Score'] if (row['Doc Name'] == 'News') else news
            weather = weather+row['TF_IDF Score'] if (row['Doc Name'] == 'Weather') else weather
            rfm = rfm+row['TF_IDF Score'] if (row['Doc Name'] == 'Random famous quotes') else rfm
            syn = syn+row['TF_IDF Score'] if (row['Doc Name'] == 'Synonym') else syn
            jokes = jokes+row['TF_IDF Score'] if (row['Doc Name'] == 'Jokes') else jokes
            gt = gt+row['TF_IDF Score'] if (row['Doc Name'] == 'Global Time') else gt

        res = pd.DataFrame({'Word': [_word],'Wikipedia': [wiki],"News":[news],
                    "Weather":[weather],"Random famous quotes":[rfm],"Synonym":[syn],"Jokes":[jokes],"Global Time":[gt]})
        TD_Matrix = TD_Matrix.append(res)        
print(TD_Matrix)
export_csv = TD_Matrix.to_csv (r"/home/simelabs/Desktop/pythonTuts/ML/TF_IDF/data/TD_Matrix.csv", index = None, header=True) 
        
    

                        
