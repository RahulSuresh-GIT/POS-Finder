import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

sample_text="rahul is a good boy"
tokenized = sent_tokenize(sample_text)

for i in tokenized:
    word=word_tokenize(i)
    tag=nltk.pos_tag(word)
    print(tag)

