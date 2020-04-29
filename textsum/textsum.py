# textsumExample to get a feel for text summerization
# importing libraries for text summerization
import io
import json
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import networkx as nx
import math
from sklearn.metrics.pairwise import cosine_similarity
from gensim.summarization.summarizer import summarize
# function to remove these stopwords from our dataset
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

# Extract word vectors
# using pre-trained Wikipedia 2014 + Gigaword 5 GloVe vectors
# you can download it @ https://nlp.stanford.edu/data/glove.6B.zip

def get_rank(myList = [],*args):
    textrank = ''
    for i in range(math.ceil(len(ranked_sentences)/3)):
        textrank += (ranked_sentences[i][1])
    return textrank

word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

# create dataframe for article to munipulate
df = pd.read_json("update.json")
with open('update.json',encoding="utf8") as data_file:
    data = json.load(data_file)

#normalize df
df_fields = pd.json_normalize(data,max_level=1)

for z in range(len(df)):
    sumtext = df_fields['fields.description'][z]

    sentences = []
    #for s in df_fields['fields.description']:
    sentences.append(sent_tokenize(df_fields['fields.description'][z]))

    sentences = [y for x in sentences for y in x] # flatten list

    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]

    stop_words = stopwords.words('english')

    # create vectors for our sentences
    sentence_vectors = []
    for i in clean_sentences:
      if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
      else:
        v = np.zeros((100,))
      sentence_vectors.append(v)

      # similarity matrix
    sim_mat = np.zeros([len(sentences), len(sentences)])

    # initialize the matrix with cosine similarity scores.
    for i in range(len(sentences)):
      for j in range(len(sentences)):
        if i != j:
          sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)

    #Summary Extraction
    ranked_sentences = ''
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    text = get_rank(ranked_sentences)
    t = summarize(text,ratio=0.15)
    if (t == ''):
        df.fields[z]['description'] = text
    else:
        df.fields[z]['description'] = t
    

x={}
for i in range(len(df)):
    temp={}
    temp["model"] = "jobs.jobsinfo"
    temp["pk"]= i
    x[i]=temp
    x[i]["fields"]={
        "JobTitle":(df.fields[i]['JobTitle']),
        "organization":(df.fields[i]['organization']),
        "description": df.fields[i]['description'],
        "salary":(df.fields[i]['salary']),
        "place":df.fields[i]['place'],
        "link":df.fields[i]['link'],
        "site":df.fields[i]['site']}
x=list(x.values())

with io.open('update_summary.json', 'w',encoding='windows-1252') as fp:
    json.dump(x,fp)
#Note: My django did not like indents so I got rid of them
