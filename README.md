
# Introduction 

This package is an aggregation of several packages I found useful for text pre-processing including gensim and ntlk. I put them together to create a more comprehensive and convenient pipeline. 

# Installation

```
pip install tokenizer_xm
```

# Usage

## Processing a single text string


```python
from tokenizer_xm import text_tokenizer_xm, contractions

# An example text
example_text = "This is an amazing product! I've been using it for almost a year now and it's clearly better\
 than any other products I've used."
```


```python
print("Original text:")
print(example_text)
print("---")

print("Simple Preprocessed:")
print("---")
tk = text_tokenizer_xm(text = example_text, lemma_flag= False, stem_flag = False, stopwords = [])
print(tk.txt_pre_pros())
print("---")

print("Pre-processing with regular contractions (e.g. I've -> I have):")
# In this package, I included a dictionary of regular contractions for your convenience
tk = text_tokenizer_xm(text = example_text, lemma_flag= False, stem_flag = False, \
                       contractions = contractions, stopwords=[])
print(tk.txt_pre_pros())
print("---")

print("Pre-processing with lemmatization:")
tk = text_tokenizer_xm(text = example_text, lemma_flag= True, stem_flag = False, \
                       contractions = contractions, stopwords=[])
print(tk.txt_pre_pros())
print("---")

print("Pre-processing with lemmatization and stemming:")
# This package uses the SnowballStemmer from ntlk.stem. I will try to make it customizable later
tk = text_tokenizer_xm(text = example_text, lemma_flag= True, stem_flag = True, \
                       contractions = contractions, stopwords=[])
print(tk.txt_pre_pros())
print("---")

print("Adding stop words")
# This package uses the SnowballStemmer from ntlk.stem. I will try to make it customizable later
tk = text_tokenizer_xm(text = example_text, lemma_flag= True, stem_flag = True, \
                       contractions = contractions, stopwords=["this",'be',"an",'it'])
print(tk.txt_pre_pros())
print("---")
```

    Original text:
    This is an amazing product! I've been using it for almost a year now and it's clearly better than any other products I've used.
    ---
    Simple Preprocessed:
    ---
    ['this', 'is', 'an', 'amazing', 'product', 've', 'been', 'using', 'it', 'for', 'almost', 'year', 'now', 'and', 'it', 'clearly', 'better', 'than', 'any', 'other', 'products', 've', 'used']
    ---
    Pre-processing with regular contractions (e.g. I've -> I have):
    ['this', 'is', 'an', 'amazing', 'product', 'have', 'been', 'using', 'it', 'for', 'almost', 'year', 'now', 'and', 'it', 'has', 'it', 'is', 'clearly', 'better', 'than', 'any', 'other', 'products', 'have', 'used']
    ---
    Pre-processing with lemmatization:
    ['this', 'be', 'an', 'amaze', 'product', 'have', 'be', 'use', 'it', 'for', 'almost', 'year', 'now', 'and', 'it', 'have', 'it', 'be', 'clearly', 'better', 'than', 'any', 'other', 'product', 'have', 'use']
    ---
    Pre-processing with lemmatization and stemming:
    ['this', 'be', 'an', 'amaz', 'product', 'have', 'be', 'use', 'it', 'for', 'almost', 'year', 'now', 'and', 'it', 'have', 'it', 'be', 'clear', 'better', 'than', 'ani', 'other', 'product', 'have', 'use']
    ---
    Adding stop words
    ['amaz', 'product', 'have', 'use', 'for', 'almost', 'year', 'now', 'and', 'have', 'clear', 'better', 'than', 'ani', 'other', 'product', 'have', 'use']
    ---


## Processing a list of text


```python
text_list = ['I am ready',"This is great","I love it"]
tk = text_tokenizer_xm(text = text_list, lemma_flag= True, stem_flag = True, \
                       contractions = contractions, stopwords=[])
# Use the .txt_pre_pros_all method instead when the input is a corpus
print(tk.txt_pre_pros_all())
print("---")
```

    0          [be, readi]
    1    [this, be, great]
    2           [love, it]
    dtype: object
    ---


## The order of stop words removal and lemmatization/stemming

The current algorithm **performs lemmatization and stem before stop-words removal**. Thus,

1. You need to be carefull when defining a list of stop words. For example, including the term "product" will also remove the term "production" if you set the stem_flag to True or the term "products" if you set lemma_flag to True.

2. When the lemma_flag is set to True, terms like "is" and "are" will be lemmatized to "be". And if "be" is not in the list of stopwords, it will remain. It is recommended that you process the list of stop-words as well if you decide to perform lemmatization


```python
"""
Example
"""

text = "products, production, is"
stop_words = ['product','is']
tk = text_tokenizer_xm(text = text, lemma_flag= False, stem_flag = False, \
                       contractions = contractions, stopwords=stop_words)
# Use the .txt_pre_pros_all method instead when the input is a corpus
print(tk.txt_pre_pros())
```

    ['products', 'production']



```python
tk = text_tokenizer_xm(text = text, lemma_flag= True, stem_flag = False, \
                       contractions = contractions, stopwords=stop_words)
# Use the .txt_pre_pros_all method instead when the input is a corpus
print(tk.txt_pre_pros())
```

    ['production', 'be']



```python
tk = text_tokenizer_xm(text = text, lemma_flag= True, stem_flag = True, \
                       contractions = contractions, stopwords=stop_words)
# Use the .txt_pre_pros_all method instead when the input is a corpus
print(tk.txt_pre_pros())
```

    ['be']

