import SentenceSplitter
import Tokenizer
import Transliterator
import Stemmer
import POSTagger
import numpy
import scipy


def mainfunctioncode():
    print("\nEnter your Sentence")
    hin: str = input()
    print("\nYour Sentence Is\n")
    # print("\n")
    print(hin)

    token_list=[]
    stem_dict=[]

    split = SentenceSplitter.code_splitter(hin)
    Transliterator.Transliterate.code_transliterate(split)
    token_list = Tokenizer.ClassTokenizer.code_tokenizer(split)
    print(token_list)
    stem_dict = Stemmer.stem(token_list)
    print("\n The Root Words are\n")
    print(stem_dict)
    print("\n The POS Tagging is as follows ")

    POSTagger.postag_code(split)


mainfunctioncode()