from indicnlp.tokenize import sentence_tokenize


#
# class ClassSplitter:

def code_splitter(string):
    sentences = sentence_tokenize.sentence_split(string, lang='hi')
    for t in sentences:
        print("\n Choosing the first Sentence")
        print(t)
        return t
