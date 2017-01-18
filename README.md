# Tagger
RDR POS Tagger implementation based on [RDRPOSTagger](http://rdrpostagger.sourceforge.net/)

# Assumption
This library assume that you are using Python 3.5 or later. Honestly, I have not tried to install this library on Python 2.7. You can try if you want to contribute.

Assumption:

 - Python 3.5
 - Only support 1 sentence
 - The sentence must be tokenized

Current supported languages:

 - Thailand

# Installation
I never try anything before, but I think there will be no error. If there is an error, you can try to install
```bash
$ > apt-get install libthai-dev
```

Installation is really straight forward, you just need to `pip install artagger`

# Quick Example
Just do a quick example if you want to use this library.
```python
>> from artagger import Tagger
>> tagger = Tagger()
>> words = tagger.tag("ผมรักคุณ")
```
The `tag()` function will return you an array of `Word`. 
```python
>> for word in words:
>>    print("%s/%s" % (word.word, word.tag))
```
Run above syntax to get any word and tag inside sentence

# CITATION
> Dat Quoc Nguyen, Dai Quoc Nguyen, Dang Duc Pham and Son Bao Pham. RDRPOSTagger: A Ripple Down Rules-based Part-Of-Speech Tagger. In Proceedings of the Demonstrations at the 14th Conference of the European Chapter of the Association for Computational Linguistics (EACL), pp. 17-20, 2014
> 
> Dat Quoc Nguyen, Dai Quoc Nguyen, Dang Duc Pham and Son Bao Pham. A Robust Transformation-Based Learning Approach Using Ripple Down Rules for Part-Of-Speech Tagging. AI Communications (AICom), vol. 29, no. 3, pp. 409-422, 2016. 
