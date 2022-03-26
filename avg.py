import csv
import pandas as pd
import plotly.figure_factory as pff

df=pd.read_csv("P-108.csv")

fig=pff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=False)
fig.show()