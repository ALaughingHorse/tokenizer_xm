"""
Define functions and tokenizers
"""
import gensim
import re
import pandas as pd

from nltk.stem import WordNetLemmatizer, SnowballStemmer
# Define a contraction dictionary
contractions = {
"ain't": "am not / are not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is",
"i'd": "I had / I would",
"i'd've": "I would have",
"i'll": "I shall / I will",
"i'll've": "I shall have / I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"}

class text_tokenizer_xm:
    
    def __init__(self,text, lemma_flag = True, stem_flag = False, stopwords = list(gensim.parsing.preprocessing.STOPWORDS),\
                contractions = None):
        self.text = text
        self.lemma_flag = lemma_flag
        self.stem_flag = stem_flag
        self.stop_words = stopwords
        self.contract_dict = contractions
        
    def txt_pre_pros(self):
        """
        Perform pre-processing for text contents

        ------Parameters
        text: the text input

        ------Output
        the stemmed and lemmatized 
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
        for token in gensim.utils.simple_preprocess(self.text):
            if token not in self.stop_words and len(token):
                result.append(token)
                
        if self.lemma_flag:
            result = [lemmatizer.lemmatize(token, pos='v') for token in result]
            result = [lemmatizer.lemmatize(token, pos='n') for token in result]
        
        if self.stem_flag:
            result = [stemmer.stem(token) for token in result]
                
        self.processed_text = result
        return result
    
    def txt_pre_pros_all(self):
        """
        When text is a collection of reviews
        """
        text_series = pd.Series(self.text)
        
        output = text_series.apply(lambda x: text_tokenizer_xm(text = x,lemma_flag=self.lemma_flag,\
                                                              stem_flag = self.stem_flag,stopwords = self.stop_words,\
                                                              contractions = self.contract_dict).txt_pre_pros())
        return output