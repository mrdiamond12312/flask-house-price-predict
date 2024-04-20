import tensorflow as tf
from typing import List

import numpy as np
import pandas as pd

from sklearn import preprocessing

model = tf.keras.models.load_model('./src/model/model.h5')

dataframe = pd.read_csv(
    './src/model/transformed-data.csv', skiprows=1, header=None)

features = dataframe.iloc[:, 1:20]

scaler = preprocessing.StandardScaler()
scaler = scaler.fit(features)


def vectorize(array: List[float]):
    scaledData = scaler.transform(np.array(array).reshape(1, -1))
    print(scaledData)
    return tf.reshape(scaledData[0], shape=(1, 19))


def predictHousePrice(array: List[float]):
    print(model.predict(vectorize(array)))
    return model.predict(vectorize(array))
