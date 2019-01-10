import pickle
import os

big_list = []
list_key = []
list_value = []
dict = {}

path = 'data/kb/' # Folder Path

for filename in os.listdir(path):
    print(path+filename)
    with open(path+filename, 'r') as f:
        contents = f.read()
        contents = (contents.replace("<http://dbpedia.org/ontology/wikiPageDisambiguates>", ''))
        contents= (contents.replace("<http://en.wikipedia.org/wiki/",''))
        contents = contents.split('\n')

        for content in contents:
            array=[]
            array.append(content)
            big_list.append(array[0].split(' '))

        for list in big_list:
            key = (list[0].replace('<http://dbpedia.org/resource/','').replace('>','').replace('_(disambiguation)','').replace('_',' '))
            # print(key)
            list_key.append(key)
            value = (list[2].replace('<','').replace('>',''))
            list_value.append(value)

        for key in list_key:
            dict[key]= []

        i = 0
        for key in list_key:
            dict[key].append(list_value[i])
            i = i+1
        print(dict)

        # pickle.dump(dict, open("output/sample_disambiguate_offline_dict.p", "wb"))
        pickle.dump(dict, open("output/disambiguate_offline_dict.p", "wb"))
