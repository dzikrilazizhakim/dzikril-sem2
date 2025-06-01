import pandas as pd
#1
file_path = r"C:\fajar\jarkom\data_penjualan.xlsx"
data = pd.read_excel(file_path, engine="openpyxl")

print(data.head())

#2
data['Total Harga'] = data['Jumlah'] * data["Harga Satuan"]
print('\nData dengan kolom Total Harga: ')
print(data.head())

#3
data_elektronik = data[data['Kategori'] == 'Elektronik']
data_elektronik.to_excel('elektronik.xlsx', index=False)
print("\nData elektronik disimpan di elektronik.xlsx")

#4
rekap = data.groupby('Kategori')['Total Harga'].sum().reset_index()
rekap.columns = ['Kategori', 'Total Pendapatan']
print("\nRekap total pendapatan per kategori: ")
print(rekap)

#5
data_sorted = data.sort_values(by='Total Harga', ascending=False)
data_sorted.to_excel('penjualan_terurut.xlsx', index=False)
print("\nData telah disimpan berdasarkan Total Harga dan disimpan di penjualan: ")