# -*- coding: utf-8 -*-
import codecs
import copy
import os

from .InitialTagger.InitialTagger import initializeSentence
from .SCRDRlearner.Object import FWObject
from .SCRDRlearner.SCRDRTree import SCRDRTree
from .Utility.Utils import getWordTag, readDictionary


class Word:
    def __init__(self, **kwargs):
        self.word = kwargs.get("word", None)
        self.tag = kwargs.get("tag", None)


class RDRPOSTagger(SCRDRTree):
    """
    RDRPOSTagger for a particular language
    """

    def __init__(self):
        self.root = None

    def tagRawSentence(self, dictionary, rawLine):
        line = initializeSentence(dictionary, rawLine)
        sen = []
        wordTags = line.split()
        for i in range(len(wordTags)):
            fwObject = FWObject.getFWObject(wordTags, i)
            word, tag = getWordTag(wordTags[i])
            node = self.findFiredNode(fwObject)
            if node.depth > 0:
                sen.append(Word(word=word, tag=node.conclusion))
                # sen.append(word + "/" + node.conclusion)
            else:  # Fired at root, return initialized tag
                sen.append(Word(word=word, tag=tag))
                sen.append(word + "/" + tag)
        return sen
        # return " ".join(sen)


# Paths
_th_rdr_path = os.path.join(
    os.path.dirname(__file__), "Models", "POS", "Thai.RDR"
)
_th_dict_path = os.path.join(
    os.path.dirname(__file__), "Models", "POS", "Thai.DICT"
)


class Tagger:
    """
    A part-of-speech tagger.

    :Example:

    tagger = Tagger(language="th")
    word_tags = tagger.tag("ฉัน กิน ข้าว")

    for wt in wordtags:
        print(wt.word, wt.tag)
    
    # ฉัน PPRS
    # กิน VACT
    # ข้าว NCMN
    """

    def __init__(self, **kwargs):
        self.__language = kwargs.get("language", "th")  # default is Thai
        self.__model = {"th": {"rdr": _th_rdr_path, "dict": _th_dict_path}}
        self.__tagger = None
        self.__ditionary = {}
        self.load_model()

    def load_model(self):
        self.__tagger = RDRPOSTagger()
        with codecs.open(
            self.__model[self.__language]["rdr"], "r", encoding="utf-8-sig"
        ) as f:
            self.__tagger.constructSCRDRtreeFromRDRfile(f.readlines())

        with codecs.open(
            self.__model[self.__language]["dict"], "r", encoding="utf-8-sig"
        ) as f:
            self.__dictionary = readDictionary(f.readlines())

    def tag(self, text):
        _text = copy.deepcopy(text)
        return self.__tagger.tagRawSentence(self.__dictionary, _text)
