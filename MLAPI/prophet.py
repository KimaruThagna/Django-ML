import pandas as pd
import seaborn as sns
bike = pd.read_csv('bike_sharing_daily.csv')
bike = bike[['dteday','cnt']]
bike.columns = ['ds','y']
print(bike.tail())