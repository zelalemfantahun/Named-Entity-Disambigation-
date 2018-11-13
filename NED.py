import nltk
from nltk import ngrams

txt = open("/home/zelalem/Desktop/data/input_data.txt")
text = txt.read()


def preprocess():

    tokenized_doc = nltk.word_tokenize(text)
    tagged_sentences = nltk.pos_tag(tokenized_doc)
    ne_chunked_sents = nltk.ne_chunk(tagged_sentences)

    # Part-Of-Speech Tagger
    for pos in tagged_sentences:
        print (pos)

    # Named Entity Recognizer
    named_entities = []
    for tagged_tree in ne_chunked_sents:
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
            entity_type = tagged_tree.label()
            named_entities.append((entity_name, entity_type))
    for names in named_entities:
        print(names)

    # ASCII Folding Filter

    # Shingle Token Filter
    num_shingle = 4
    sixgrams = ngrams(tokenized_doc, num_shingle)
    for grams in sixgrams:
        print (grams)


preprocess()

