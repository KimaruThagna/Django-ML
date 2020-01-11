from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.linear_model import LogisticRegression, LinearRegression
'''
is she mad? 
1- Mad
0- Not mad
'''
responses = [
    ["fine do what you want", 1],    ["youre dumb", 0],    ["okay bye", 1],    ["Aki wewe", 0],    ["im fine", 1],    ["wow!!", 1],["gosh", 0],
]
X, y = [], []
for i in responses: # create feature and label lists
    X.append( i[0] )
    y.append( i[1] )

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X) # transform features to allow ML model to evaluate text as vectors
classifier_1 = LogisticRegression() # since its regression, closer to 1 means Mad, closer to 0 means not mad
classifier_2 = LinearRegression()
classifier_1.fit(X_vectorized, y) # fit classifier
classifier_2.fit(X_vectorized, y) # fit classifier
# perform test
tests = [vectorizer.transform(["fine"]), vectorizer.transform(["aki you"])]
for item in tests:
    print(f'Prediction1{classifier_1.predict(item)}')
    print(f'Prediction2{classifier_2.predict(item)}')
