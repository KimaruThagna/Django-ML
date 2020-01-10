from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.linear_model import LogisticRegressionCV, LinearRegression
'''
is she mad? 
1- Mad
0- Not mad
'''
responses = [
    ["fine do what you want", 1],
    ["youre dumb", 0],
    ["okay bye", 1],
    ["Aki wewe", 0],
    ["im fine", 1],
    ["wow!!", 1],
]
X, y = [], []
for i in responses: # create feature and label lists
    X.append( i[0] )
    y.append( i[1] )

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X) # transform features to allow ML model to evaluate text as vectors
classifier = LogisticRegressionCV() # since its regression, closer to 1 means Mad, closer to 0 means not mad
classifier.fit(X_vectorized, y) # fit classifier
