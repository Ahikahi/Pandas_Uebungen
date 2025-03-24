#Öffnen Sie K3-iris-1 und lassen Sie das Programm ablaufen:
#	• Analysieren und kommentieren Sie das komplette Programm.

#	• Wie viele Hidden-Layer / Knoten hat das KNN?
# HiddenLayer = 3
# Knoten = 99

#	• Versuchen Sie die Korrektklassifizierungsrate zu erhöhen. Welche Möglichkeiten kennen Sie?
# Iterationen erhöhen
# Aktiverungsfunktion ändern
# mehr hiddenlayer
# mehr knoten


import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

path = "csv_dateien/iris (1).csv"
data = pd.read_csv(path, delimiter=',')
print(data.head())

"""Daten vorbereiten."""

# Was soll vorhergesagt werden? Spaltenname in Variable speichern.
col_name = 'species'

# Zeichenkette in Zahlen umwandeln
data[col_name] = data[col_name].astype('category')
data[col_name] = data[col_name].cat.codes

# Hier findet die Aufteilung in zwei Tabellen statt (Input=data und Output=col).
col = data[col_name]
data = data.drop([col_name], axis = 1)

"""KNN aufbauen"""

# Aus den zwei Tabellen vier Tabellen erzeugen
train_data, test_data, train_col, test_col = train_test_split(data,col, test_size=0.2, random_state=42)

# Aufbau KNN
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(4,)))
model.add(tf.keras.layers.Dense(32, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(42, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))


# Konfiguration des Lernprozesses
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

"""Trainieren"""

# 30 Durchläufe
model.fit(train_data, train_col, epochs=45)

"""Testen"""

test_loss, test_acc = model.evaluate(test_data, test_col)
print('Test accuracy:', test_acc)