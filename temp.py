# Pandas Dataframe from Dicts of series.
import pandas as pd
d = {'one' : pd.Series([10, 20, 30, 40],index =['a', 'b', 'c', 'd']),'two' : pd.Series([10, 20, 30, 40],index =['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)