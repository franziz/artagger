from .Utility.Utils import getWordTag, readDictionary
from .InitialTagger.InitialTagger import initializeSentence
from .SCRDRlearner.SCRDRTree import SCRDRTree
from .SCRDRlearner.Object import FWObject
import os
import copy
import pickle

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
            else:# Fired at root, return initialized tag
                sen.append(Word(word=word, tag=tag))
                sen.append(word + "/" + tag)
        return sen
        # return " ".join(sen)

class Tagger:
    def __init__(self, **kwargs):
        self.language = kwargs.get("language", "th")
        self.text = kwargs.get("text", None)
        self.model = {}
        self.load_model()

    def load_model(self):
        self.model.update({"th":{
            "rdr": open(os.path.join(os.path.dirname(__file__), "Models", "POS", "Thai.RDR"), "r"),
            "dict": open(os.path.join(os.path.dirname(__file__), "Models", "POS", "Thai.DICT"), "r")
        }})

    def tag(self, text):
        self.text = copy.copy(text)
        tagger = RDRPOSTagger()

        rdr_file = self.model[self.language]["rdr"]
        dict_file = self.model[self.language]["dict"]

        tagger.constructSCRDRtreeFromRDRfile(rdr_file.readlines())
        dictionary = readDictionary(dict_file.readlines())
        return tagger.tagRawSentence(dictionary, self.text)