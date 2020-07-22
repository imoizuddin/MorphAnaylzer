import SentenceSplitter
import Tokenizer
import Transliterator
import Stemmer
import POSTagger


def mainfunctioncodet(String):
    # hin: str = String
    # split = SentenceSplitter.code_splitter(hin)
    # Transliterator.Transliterate.code_transliterate(split)
    token_list = Tokenizer.ClassTokenizer.code_tokenizer(String)
    listToStr = "' , '" .join([str(elem) for elem in token_list])
    return listToStr


def mainfunctioncodestem(String):
    stringtrimmed = String.strip()
    token_list = Tokenizer.ClassTokenizer.code_tokenizer(stringtrimmed)
    stem_dict = Stemmer.stem(token_list)
    return stem_dict


def mainfunctioncodepos(String):
    posTag = POSTagger.postag_code(String)
    return posTag
