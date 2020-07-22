from nltk.tag import tnt
from nltk.corpus import indian
import nltk


def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger


def postag_code(string: object) -> object:
    model = hindi_model()
    new_tagged = (model.tag(nltk.word_tokenize(string)))
    # print(new_tagged)
    return new_tagged

