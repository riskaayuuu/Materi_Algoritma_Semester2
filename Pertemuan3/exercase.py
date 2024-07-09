nama = str(input('Masukkan Nama Karyawan : '))
jam_kerja = int(input(' Jam kerja dalam satu hari : '))
Tarif = float(input('Tarif per jam : '))

jumlah_jam_kerja = jam_kerja* 20
jumlah_gaji_perbulan = (jumlah_jam_kerja * Tarif)
print('\n')

print(f'Nama karyawan  : {nama}')
print(f'Jumlah gaji perbulan : {jumlah_gaji_perbulan}')


# daftar_belanja =(input('Masukan daftar belanja:'))
