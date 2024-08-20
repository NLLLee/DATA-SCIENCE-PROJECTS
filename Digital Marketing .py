
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from jedi.api.refactoring import inline

file_location = '/Users/nengliangli/Downloads/RXMG_Assessment_Data.xlsx'
df = pd.read_excel(file_location)
Clicks = df['Clicks']
Revenue = df['Revenue']

def best_fit(Clicks,Revenue):
    xbar = sum(Clicks)/len(Clicks)
    ybar = sum(Revenue)/len(Revenue)
    n = len(Clicks) # or len(Revenue)

    numer = sum([xi*yi for xi,yi in zip(Clicks, Revenue)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in Clicks]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a,b

a, b = best_fit(Clicks,Revenue)

plt.figure(figsize=(10,5))
plt.xticks(rotation=45)
plt.xlabel('Clicks')
plt.ylabel('Revenue')
plt.title('Revenue vs Clicks Graph')
plt.scatter(Clicks,Revenue, color='blue')
yfit= [a + b * Clicksi for Clicksi in Clicks]
plt.plot(Clicks, yfit)
plt.tight_layout()
plt.grid()
plt.show()