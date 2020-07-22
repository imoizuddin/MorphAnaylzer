from indicnlp.tokenize import sentence_tokenize


def code_splitter(string):
    sentences = sentence_tokenize.sentence_split(string, lang='hi')
    for t in sentences:
        return t
