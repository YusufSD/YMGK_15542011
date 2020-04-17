import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('MadenManisa.csv',parse_dates=['Tarih'],index_col=['Tarih'])
df=pd.DataFrame(data)
df.info()

df=pd.DataFrame(data)
df=(df-df.min())/(df.max()-df.min())
df=df.fillna(df.mean())
pm10= df.PM10.resample('M').mean().plot()
so2= df.SO2.resample('M').mean().plot()
co= df.CO.resample('M').mean().plot()
no2= df.NO2.resample('M').mean().plot()
nox= df.NOX.resample('M').mean().plot()
no= df.NO.resample('M').mean().plot()
o3= df.O3.resample('M').mean().plot()
plt.title("Ölçüm Değerleri Aylık Değişimi")
plt.legend(loc='best')
plt.show()
co= df.CO.resample('H').mean().plot()
O3= df.O3.resample('H').mean().plot()
pm10= df.NO2.resample('M').mean().plot(kind='bar', color='black',edgecolor='white', width=1)
