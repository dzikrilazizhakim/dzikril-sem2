import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Data_Penduduk.xlsx')
profession_counts = data['Profesi'].value_counts()
plt.figure(figsize=(10, 6))

plt.pie(profession_counts, labels=profession_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Profesi Warga Desa Cibodas')
plt.axis('equal')
plt.show()
