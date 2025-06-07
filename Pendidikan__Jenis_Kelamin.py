import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Data_Penduduk.xlsx')

grouped = data.groupby(['Pendidikan_Terakhir', 'Jenis_Kelamin']).size().unstack()

grouped.plot(kind='bar', figsize=(20, 6))
plt.title("Perbandingan Jumlah Warga Berdasarkan Pendidikan dan Jenis Kelamin")
plt.xlabel("Pendidikan Terakhir")
plt.ylabel("Jumlah Warga")
plt.xticks(rotation=45)
plt.legend(title="jenis Kelamin")
plt.tight_layout()
plt.show()
