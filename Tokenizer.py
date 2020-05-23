from indicnlp.tokenize import indic_tokenize


class ClassTokenizer:

    def code_tokenizer(string):
        # print('\nInput String: {}'.format(string))
        # print('\nTokens: ')
        list = []
        for t in indic_tokenize.trivial_tokenize(string):
            list.append(t)

        return list
