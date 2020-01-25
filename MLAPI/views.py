from django.shortcuts import render
from .apps import MlapiConfig
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.

'''
https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
https://www.kaggle.com/cedriclacrambe/keras-gpt-2-text-generation-tests
https://www.freecodecamp.org/news/how-to-apply-reinforcement-learning-to-real-life-planning-problems-90f8fa3dc0c5/
https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-location-data-5c1e033d0a5a
https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-deep-learning-f46d44afb8a6
https://link.medium.com/q5vnU2d962
https://link.medium.com/zX4Bnsb962
'''


class she_mad_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get statement from boo
            statment = request.GET.get('statement')
            # vectorize statement
            vector = MlapiConfig.vectorizer.transform([statment])
            # predict based on vector
            prediction = MlapiConfig.regressor.predict(vector)[0]
            # build response
            response = {'is she mad?': str(prediction)}
            # return response
            return JsonResponse(response)