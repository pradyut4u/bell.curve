import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv(r"D:/python/py/bell_curve.csv")
digram = pff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"])
digram.show()