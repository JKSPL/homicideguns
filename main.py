import learn as learn
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

with open("homicide.txt") as file:
    homicide_df = pd.read_html(file.read())[0]
with open("guns.txt") as file:
    guns_df = pd.read_html(file.read())[0]

guns_df = guns_df.rename(columns={
    'Countries and territories': 'Country'
})
homicide_df = homicide_df.rename(columns={
    'Country (or dependent territory, subnational area, etc.)': 'Country',
    'Rate': 'Homicide Rate'
})
guns_df = guns_df.set_index("Country")
homicide_df = homicide_df.set_index("Country")
homicide_df = homicide_df[homicide_df['Region'] == 'Europe']

all_df = homicide_df.join(guns_df).dropna()
print(all_df.columns)
plt.figure(figsize=(10, 10), dpi=300)

ax = all_df.plot.scatter(x='Estimate of civilian firearms per 100 persons', y='Homicide Rate')
for k, v in all_df.iterrows():
    p = (v['Estimate of civilian firearms per 100 persons'], v['Homicide Rate'])
    ax.annotate(k, p, fontsize=6)

X = all_df['Estimate of civilian firearms per 100 persons'].values.reshape(-1, 1)
Y = all_df['Homicide Rate'].values.reshape(-1, 1)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.plot(X, Y_pred, color='red')
plt.show()


