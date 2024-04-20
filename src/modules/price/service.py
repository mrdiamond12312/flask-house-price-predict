import tensorflow as tf
from typing import List

import numpy as np
import pandas as pd

from sklearn import preprocessing
from joblib import load

dataframe = pd.read_csv(
    './src/model/transformed-data.csv', skiprows=1, header=None)

features = dataframe.iloc[:, 1:20]

scaler = preprocessing.StandardScaler()
scaler = scaler.fit(features)


model_ann = tf.keras.models.load_model('./src/model/model.h5')

model_regression = load('./src/model/reg-model.joblib')


def vectorize(array: List[float]):
    scaledData = scaler.transform(np.array(array).reshape(1, -1))
    return tf.reshape(scaledData[0], shape=(1, 19))


def predictHousePriceUsingANN(array: List[float]):
    return model_ann.predict(vectorize(array))[0][0]

def predictHousePriceUsingLR(array: List[float]):
    return model_regression.predict(vectorize(array))[0]