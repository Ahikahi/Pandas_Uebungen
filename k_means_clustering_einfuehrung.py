import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

# Datei laden
path = "csv_dateien/iris (1).csv"

data = pd.read_csv(path, delimiter=',')

# Daten ohne Zielspalte erzeugen
data_unknown = data.drop(['species'], axis=1)

print(data_unknown.head)

model = KMeans()

# Ermittle optimale Anzahl von Klassen
visualizer = KElbowVisualizer(model, k=(2, 9))
visualizer.fit(data_unknown)
visualizer.show()

# n_clusters wird nach der graphischen Analyse initialisiert
kmeans = KMeans(n_clusters=4)

# Vorhersage der Klassen
pred = kmeans.fit_predict(data_unknown)

# Zusammenfügen der Datensätze (Spalten)
data_new = pd.concat([data, pd.DataFrame(pred, columns=['label'])], axis=1)
print(data_new)

# Speichern in neue CSV Datei
data_new.to_csv("csv_datein/data_new.csv")