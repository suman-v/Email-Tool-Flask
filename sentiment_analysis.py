import pandas as pd
import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')
data = pd.read_csv(r"C:\Users\User\Downloads\chrome_reviews.csv")
data = data['Text']


data = (data)

import sys, re
from termcolor import colored, cprint
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")

# remove special characters and remove stop words from text
def clean_text(i):
    print (i)
    i = i.replace('&', '').replace('(', '').replace(')','').replace('[','').replace(']','')
    i = i.replace('\'', '').replace('\\', '')
    i = i.replace('.', '').replace('%', '').replace('/','')
    i = i.replace('"', '').replace('*', '').replace(':', '')
    i = str.lower(i)
    i = re.sub(" \d+", " ", i)
    i = ' '.join([word for word in i.split() if word not in cachedStopWords])  
    print (i)
    return i


clean_text(data)
# import nltk
# from nltk.stem import WordNetLemmatizer
# from termcolor import colored, cprint
# import spacy 
# nlp = spacy.load("en_core_web_sm")

# # nltk.download('wordnet')
# stemmer = WordNetLemmatizer()
# c = 0
# document = ''
# for i in data.INGREDIENTS:

#     try: 
#         text = clean_text(i)
#         doc = nlp(text)
#         words = [token.text for token in doc]  # tokenization
#         words = [stemmer.lemmatize(i) for i in words]  # lemmetization
        
#         sen = ''
#         for i in words:
#             sen = " ".join((sen, i)) 

#         document = " ".join((document, sen))
#         c+=1
        
#     except:
#         print ('error') # handling nan values in data
        
        
        
        
        
        
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
  
hotel_rev = [“Great place to be when you are in Bangalore.”,
“The place was being renovated when I visited so the seating was limited.”,
“Loved the ambience, loved the food”,
“The food is delicious but not over the top.”,
“Service - Little slow, probably because too many people.”,
“The place is not easy to locate”,
“Mushroom fried rice was tasty”]
  
sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print(‘{0}: {1}, ‘.format(k, ss[k]), end=’’)
     print()