import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
date = [datetime.datetime(2018, 1, 1) + datetime.timedelta(days=x) for x in range(0, 365)]
value = list(np.random.randint(low=0, high=100, size=365))
df['date'] = pd.to_datetime(date)
df.index = df['date']
df['value'] = value
print(df['date'])
print(df['value'])
# diseña un gráfico de barras para mostrar la media de datos por trimestre

x = df.groupby(df['date'].dt.quarter).mean()
x.plot.barh()
