Nama = input('Masukkan Nama: ')
Umur = int(input('Masukkan Umur: '))
pekerjaan_orang_tua = input('Masukkan Pekerjaan: ')
gaji_orang_tua = int(input('Gaji Orang Tua: '))
ipk = float(input('ipk: '))

pekerjaan = ['dokter', 'PNS', 'Polisi']
if(pekerjaan_orang_tua is not pekerjaan) and (gaji_orang_tua <=1000000) and (Umur <= 25) and (ipk >= 2.7):
    print('SELAMAT KAMU DAPAT BEASISWA YEAYY')
else:
    print('MAAF, KAMU BELUM BERUNTUNG')    
