import numpy as np
import pandas as pd
import json
import lxml
from lxml import etree

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

#Reading the JSON File
mylist = []
def getKeys(obj, parent="obj") :
    global mylist
    for i in obj.keys():
        mylist.append(parent+"/"+i)
        try:
            getKeys(obj[i], parent+"/"+i)
        except AttributeError:
            pass
with open("LnT/Broker_Application_XML.json", "r") as f:
  data = json.load(f)
getKeys(data)
del mylist[0]
new_list = []
list_pair_json = []
for i in range(len(mylist)):
    arr = mylist[i].split('/')
    new_list.append(arr[-1])
    list_pair_json.append((str(arr[-1]),str(mylist[i])))
#print(new_list)

#Reading the XML File
xml_list = []
list_pair_xml = []
with open('LnT/ACORD_XML_For_SubmittionToCarrier.xml', 'r') as f:
    root = etree.parse(f)
    for e in root.iter():
        path = root.getelementpath(e)
        #print(path)
        xml_list.append(path)
del xml_list[0]
new_xml_list = []
for i in range(len(xml_list)) :
    arr1 = xml_list[i].split('/')
    new_xml_list.append(arr1[-1])
    list_pair_xml.append((str(arr1[-1]),str(xml_list[i])))
#print(new_xml_list)

#Reading the csv file
df = pd.read_csv('LnT/TestCSV.csv')


json_list = new_list
Logical_Key = df['Field_Name'].tolist()
embeddings_distilbert = model.encode(Logical_Key)

#Cosine Similarity
def find_similar(vector_representation, all_representations, k=1):
    similarity_matrix = cosine_similarity(vector_representation, all_representations)
    similarities = similarity_matrix[0]
    if k == 1:
        return [np.argmax(similarities)]
    elif k is not None:
        return np.flip(similarities.argsort()[-k:][::1])

#Get Logical Key
def get_logical_key(physical_key) :
    search_string = physical_key
    search_vect = model.encode([search_string])
    k = 1
    distil_bert_similar_indexes = find_similar(search_vect,embeddings_distilbert,k)
    output_data = []
    for index in distil_bert_similar_indexes :
        output_data.append(Logical_Key[index])
    return output_data

#Printing the values
l1 = []
for val1 in json_list :
    string = str(get_logical_key(val1))
    for i in range(len(list_pair_json)) :
        if(val1 == list_pair_json[i][0]) :
            l1.append((list_pair_json[i][1],string))
            break
l2 = []
for val1 in new_xml_list :
    string = str(get_logical_key(val1))
    for i in range(len(list_pair_xml)) :
        if(val1 == list_pair_xml[i][0]) :
            l2.append((list_pair_xml[i][1],string))
            break
res = []
for a,b in l1:
    for c,d in l2:
        if(b == d) :
            res.append((a,c))

for a,b in res:
    print(a," : ",b)
print(len(res))









