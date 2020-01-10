from sklearn.feature_extraction.text import CountVectorizer
import pickle
'''
is she mad? Finally, lets understand women
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