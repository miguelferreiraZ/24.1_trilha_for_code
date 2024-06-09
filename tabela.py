import pandas as pd
import matplotlib.pyplot as plt

def plot(x, y):
  # x, y plot to graphic bars
  plt.bar(x, y)
  tituloX = x.name
  tituloY = y.name
  plt.title(f"{tituloX} x {tituloY}")
  plt.xlabel(f"{tituloX} (Zoom to see better)")
  plt.ylabel(f"{tituloY}")
  
  plt.show()

dados = pd.read_csv("mt_cars.csv")

dados = dados.rename({"Unnamed: 0": "Modelo", "mpg": "Milhas/Galao", "cyl": "nCilidros", "disp": "Cilindradas", "hp": "Potencia", "drat": "Eixo Traseiro", "wt": "Peso", "qsec": "T(s) 1/4 milha", "vs": "Tipo Motor", "am": "Transmissao", "gear": "nMarchas", "carb": "nCarburadores"}, axis='columns')

plot(dados["Modelo"], dados["T(s) 1/4 milha"])