from indictrans import Transliterator


class Transliterate:
    def code_transliterate(self):
        trn = Transliterator(source='hin', target='eng', build_lookup=True)
        eng = trn.transform(self)
        return eng
