#Öffnen Sie K3-iris-2. Was ist an diesem Programm anders? Welche Unterschiede sind im Quellcode aufgefallen?
#Versuchen Sie die Korrektklassifizierungsrate zu erhöhen
# Die KI hat wahrscheinlich die Trainingsdaten auswendig gelernt
# Die Korrektklassifizierungsrate ist bei 100%




import tensorflow as tf
#import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

path = "csv_dateien/iris (1).csv"
data = pd.read_csv(path, delimiter=',')
print(data.head())

"""Daten vorbereiten."""

# Was soll vorhergesagt werden? Spaltenname in Variable speichern.
col_name = 'species'

# Zeichenkette in OHE umwandeln, Ergebnis in neuer Tabelle
col = pd.get_dummies(data[col_name], dtype=float)
print(col.head())

# Aus der ursprünglichen Tabelle werden die species entfernt
data = data.drop([col_name], axis = 1)
#Somit zwei Tabellen vorhanden

"""KNN aufbauen"""

# Aus den zwei Tabellen vier Tabellen erzeugen
train_data, test_data, train_col, test_col = train_test_split(data,col, test_size=0.2, random_state=42)

# Aufbau KNN
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(4,)))
model.add(tf.keras.layers.Dense(32, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))
# Konfiguration des Lernprozesses
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

"""Trainieren"""

# 50 Durchläufe
model.fit(train_data, train_col, epochs=50)

"""Testen"""

test_loss, test_acc = model.evaluate(test_data, test_col)
print('Test accuracy:', test_acc)