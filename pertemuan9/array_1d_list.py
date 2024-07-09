#Deklarasi Array 1D
nilai_siswa = [90,60,30,40,60]

#Akses Nilai Array
print(nilai_siswa[3])

#tambah data array menggunakan 'append'
nilai_siswa.append(100) 
print(nilai_siswa) #[90,60,30,40,60,100]


#menghapus nilai pada data list menggunakan 'pop' (kalau tidak ditambah angka dalam index otomatis terhapus nilai terakhir) 
nilai_siswa.pop(3)
print(nilai_siswa) #[90,60,30,60,100]


jumlah_data = len(nilai_siswa)
total_data = sum(nilai_siswa)
rata_rata = total_data/jumlah_data
nilai_tertinggi = max(nilai_siswa)
nilai_terendah = min(nilai_siswa)

jumlah_nilai_diatas_rata_rata = sum(True for i in nilai_siswa if i > rata_rata)
nilai_diatas_rata_rata = [i for i in nilai_siswa if i > rata_rata]

nilai_siswa.sort() # mengurutkan nilai terkecil ke terbesar
nilai_siswa.reverse()# membalikkan nilai akhir menjadi nilai awal

print(f'Jumlah data : {jumlah_data}')
print(f'Total data : {total_data}')
print(f'Rata-rata nilai : {rata_rata}')
print(f'Nilai tertinggi : {nilai_tertinggi}')
print(f'Nilai terendah : {nilai_terendah}') 
print(f'Jumlah Nilai Diatas rata-rata : {jumlah_nilai_diatas_rata_rata}') 
print(f'Nilai Diatas rata-rata : {nilai_diatas_rata_rata}') 
print(f'Data Urut : {nilai_siswa}')

#contoh fungsi 'reverse'
data = [8,9,976,34,5]
data.reverse()
print(data)
