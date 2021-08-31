"""
Define functions and tokenizers
"""
import re
import pandas as pd
from constants import contractions
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re


class TextPreProcessor:
    
    def __init__(self, text, lemma_flag = True, stem_flag = False, stopwords = list(set(stopwords.words("english"))),\
                contractions = contractions):
        self.text = text
        self.lemma_flag = lemma_flag
        self.stem_flag = stem_flag
        self.stop_words = stopwords
        self.contract_dict = contractions
        
    def process(self):
        """
        Perform pre-processing for text contents
        """
        stemmer = SnowballStemmer("english")
        lemmatizer = WordNetLemmatizer()
        
        result = []
        
        # If a contraction dictionary is provided. Remove the contractions
        if self.contract_dict is not None:          
            for word in self.text.split():
                if word.lower() in self.contract_dict:
                    self.text = self.text.replace(word, self.contract_dict[word.lower()])

        # Simple pre-processing to remove tokens
        # for token in gensim.utils.simple_preprocess(self.text):
        #     if len(token):
        #         result.append(token)
        text = re.sub(r'[^\w\s]','',self.text)
        result = word_tokenize(text.lower())
                
        if self.lemma_flag:
            result = [lemmatizer.lemmatize(token, pos='v') for token in result]
            result = [lemmatizer.lemmatize(token, pos='n') for token in result]
        
        if self.stem_flag:
            result = [stemmer.stem(token) for token in result]

        # remove the stopwords at last. 
        final_result = [x for x in result if x not in self.stop_words] 
        
        self.processed_text = final_result
        return final_result

    
