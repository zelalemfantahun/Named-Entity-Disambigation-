import spacy
import pickle
import re
import numpy
from nltk.corpus import stopwords
import sys

english_stopwords = stopwords.words('english')
nlp = spacy.load('en_core_web_sm')
text = str(input("Enter Sentence: "))
# txt = open("data/input_data.txt")
# text = txt.read().replace('.','')
offline_dic = open('output/disambiguate_offline_dict.p', 'rb')
offline_dic = pickle.load(offline_dic)


class Named_entity_disambig:

    def __init__(self):
        pass

    def Candidate_generation(self):

        doc = nlp(text)
        named_entity_dict = {}
        named_entity_key_list = []
        named_entity_value_list = []
        entity_from_text_list =[]
        offline_dic_list= []
        matched_element_list =[]

        for ent in doc.ents:
            named_entity = (str(ent.text)+':' +str(ent.label_))
            named_entity= (named_entity.split(':'))
            named_entity_key = named_entity[0].replace('\n','')
            named_entity_key_list.append(named_entity_key)
            named_entity_value = named_entity[1].replace('\n','')
            named_entity_value_list.append(named_entity_value)
        for key in named_entity_key_list:
            named_entity_dict[key] = []
        i = 0
        for key in named_entity_key_list:
            named_entity_dict[key].append(named_entity_value_list[i])
            i = i + 1

        entities = "ORG PERSON LOC GPE".split()
        for entity in entities:
            entity_from_text= [k for k, v in named_entity_dict.items() if entity in v]
            for item in entity_from_text:
                entity_from_text_list.append(item)


        if not entity_from_text_list:
            print(' ')
            print('No named entity found in the input text')
            print('========================================')
        else:
            print(' ')
            print('Entities which are identified from the input sentence')
            print('======================================================')
            print(entity_from_text_list)

        for key, value in offline_dic.items():
            offline_dic_list.append(key)

        for item in entity_from_text_list:
             for item1 in offline_dic_list:
                if item == item1:
                    matched_element_list.append(item)

        big_final_dict = []
        for i in matched_element_list:
            candidate_list = [v for k, v in offline_dic.items() if str(k) == str(i)]
            final_dict= dict(zip(i.split('\n'), candidate_list))
            big_final_dict.append(final_dict)

        if not big_final_dict:
                print("No Match found in the KB")
                sys.exit(0)
        else:
            return big_final_dict

    def candidate_ranking(self, big_final_dict):
        print(' ')
        print("Disambiguated Entity Link")
        print("==========================")
        big_list = []

        for dict in big_final_dict:
            for dict_value in dict.values():
                temp = []
                for i in dict_value:
                    x = (i.split("http://dbpedia.org/resource/"))
                    y = list(filter(None, x))
                    yy = (y[0].split('_'))
                    str = ''
                    for x in yy:
                        str = str + x + ' '
                    str = str[:-1]
                    temp.append(str)
                big_list.append(temp)

        big_arr2 = []
        for small_list in big_list:
            arr2 = []
            for i in small_list:
                arr2.append(re.sub(r'[^\w\s]', '', (i)))

            big_arr2.append(arr2)

        input_text_cleaned = re.sub(r'[^\w\s]', '', text)
        arr1 =input_text = input_text_cleaned.split()# remove stop words
        arr1=content = [w for w in arr1 if w.lower() not in english_stopwords]

        for arr2 in big_arr2:
            a=numpy.zeros(shape=(len(arr2), len(arr1)))
            for i in range(len(arr1)):
                for j in range(len(arr2)):
                    if arr1[i] in arr2[j]:
                        a[j][i] = 1
                    else:
                        a[j][i] = 0

            rows = len(a)
            cols = len(a[0])
            highest = []

            for x in range(0, rows):
                rowtotal = 0
                for y in range(0, cols):
                    rowtotal = rowtotal + int(a[x][y])
                highest.append(rowtotal)

            highest_value = highest.index(max(highest))
            ranked_entity= arr2[highest_value]
            print('Ambiguous word:'+ranked_entity+'     '+'Disambiguation link'+' ' +'http://dbpedia.org/resource/'+(ranked_entity).replace(' ','_'))


NED = Named_entity_disambig()
big_final_dict = NED.Candidate_generation()
NED.candidate_ranking(big_final_dict)

