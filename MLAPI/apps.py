from django.apps import AppConfig
from django.conf import settings
import os, pickle

class MlapiConfig(AppConfig):
    name = 'MLAPI'
    path = os.path.join(settings.ML_MODELS, 'pickled_models.p')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    regressor = data['regressor']
    logistic = data['logistic']
    vectorizer = data['vectorizer']