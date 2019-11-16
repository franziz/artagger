# ARTagger

[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/) 
[![pypi](https://img.shields.io/pypi/v/artagger.svg)](https://pypi.python.org/pypi/artagger)
[![PyPi downloads](https://pypip.in/d/artagger/badge.png)](https://crate.io/packages/artagger/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A Ripple Down Rules-based (RDR) Part-Of-Speech Tagger implementation based on [RDRPOSTagger](http://rdrpostagger.sourceforge.net/).

## Assumption

This library assume that you are using Python 3.5 or later. Honestly, I have not tried to install this library on Python 2.7. You can try if you want to contribute.

Assumption:

 - Python 3.5
 - Only support 1 sentence
 - The sentence must be tokenized

Current supported languages:

 - Thai

# Installation

Installation is really straight forward, just:
```bash
pip install artagger
```

You may need `libthai-dev` for Thai word segmentation. On Debian and Ubuntu, try:
```bash
apt-get install libthai-dev
```

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

Run above syntax to get any word and tag inside sentence.

# CITATION

- Dat Quoc Nguyen, Dai Quoc Nguyen, Dang Duc Pham and Son Bao Pham. [RDRPOSTagger: A Ripple Down Rules-based Part-Of-Speech Tagger](http://www.aclweb.org/anthology/E14-2005). In *Proceedings of the Demonstrations at the 14th Conference of the European Chapter of the Association for Computational Linguistics*, EACL 2014, pp. 17-20, 2014. [[.PDF]](http://www.aclweb.org/anthology/E14-2005) [[.bib]](http://www.aclweb.org/anthology/E14-2005.bib)

- Dat Quoc Nguyen, Dai Quoc Nguyen, Dang Duc Pham and Son Bao Pham. [A Robust Transformation-Based Learning Approach Using Ripple Down Rules for Part-Of-Speech Tagging](http://content.iospress.com/articles/ai-communications/aic698). *AI Communications* (AICom), vol. 29, no. 3, pp. 409-422, 2016. [[.PDF]](http://arxiv.org/pdf/1412.4021.pdf) [[.bib]](http://rdrpostagger.sourceforge.net/AICom.bib)
