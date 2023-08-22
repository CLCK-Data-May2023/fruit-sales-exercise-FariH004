import pandas as pd 
df = pd.DataFrame({'Apples': [32, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
df.to_csv('fruit.csv', index=False)
print("DataFrame saved as 'fruit.csv'")
