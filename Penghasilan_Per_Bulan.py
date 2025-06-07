import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Data_Penduduk.xlsx')

def kategori_penghasilan(penghasilan):
    if penghasilan < 2000000:
        return "Sangat Rendah"
    elif penghasilan <= 5000000:
        return "Rendah"
    elif penghasilan <= 10000000:
        return "Menengah"
    else:
        return "Tinggi"
    
data['Kategori_Penghasilan'] = data['Penghasilan_Per_Bulan'].apply(kategori_penghasilan)

penghasilan_counts = data['Kategori_Penghasilan'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(penghasilan_counts, labels=penghasilan_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribusi Kategori Penghasilan Warga")
plt.axis("equal")
plt.tight_layout()
plt.show()