import matplotlib.pyplot as plt
import pandas as pd
#import data file
starbucks = pd.read_csv("data/starbucks/directory.csv")
#Statistics of the number of Starbucks in each country grouped by country
count = starbucks.groupby(['Country']).count()
#plot
count['Brand'].plot(kind='bar', figsize=(20, 8))
plt.show()


