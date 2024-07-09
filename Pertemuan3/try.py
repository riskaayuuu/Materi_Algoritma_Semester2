nama_karyawan = input('Masukan nama karyawan:')
jam_kerja = int(input('Masukkan jam keja:'))
tarif_perjam = float(input('masukkan tarif perjam:'))

jumlah_jam_kerja = 20
total_kerja = (jam_kerja*jumlah_jam_kerja)
total_gaji = (total_kerja*tarif_perjam)
# print('==================================')
# print('total gaji yang diperoleh',nama_karyawan,'yaitu :',total_gaji)

print(f'nama karyawan: {nama_karyawan}')
print(f'jumlah gaji yang diperoleh: {total_gaji}')