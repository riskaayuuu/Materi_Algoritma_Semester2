from collections import deque
antrian = deque()
def front():
    if len(antrian) == 0:
        print(f'Antrian Sekarang : Tidak Ada Antrian')
    else:
        print(f'Antrian Sekarang : Pelanggan {antrian[0]} sedang di CS')

def queue_next():
    if len(antrian) < 2:
        print(f'Pelanggan Selanjutnya: Tidak Ada Antrian Selanjutnya')
    else:
        print(f'Pelanggan Selanjutnya : Pelanggan {antrian[1]}')

def size():
    print(f'Jumlah Antrian : {len(antrian)}')

def tambah_Antrian():
    pelanggan = input('Masukkan Nama Pelanggan : ')
    antrian.append(pelanggan)
    print(f'{pelanggan} Berhasil Ditambahkan Kedalam Antrian')
    print(35*'=')

def hapus_Antrian():
    if len(antrian) == 0:
        print('Data Kosong : Tidak Bisa Dihapus')
    else:
        antrian.popleft()
        print(f'Pelanggan Selanjutnya : {antrian[0]}')
    print(35*'=')

def lihat_Antrian():
    if len(antrian) == 0:
        print('Tidak Ada Antrian')
    else:
        print('===== Daftar Antrian =====')
        for index,value in enumerate(antrian):
            print(f'{index} : {value}')
    print(35*'=')

def tampilan():
    front()
    queue_next()
    size()
    print('''Pilihan
          1. Tambah Antrian
          2. Antrian Selanjutnya
          3. Lihat Antrian
          4. Keluar''')
    pilihan = input('Masukkan Pilihan : ')
    if pilihan == '1':
        tambah_Antrian()
    elif pilihan == '2':
        hapus_Antrian()
    elif pilihan == '3':
        lihat_Antrian()
    elif pilihan == '4':
        exit()
    else:
        print(35*'=')
        print('Masukkan Pilihan Yang Valid!')
        print(35*'=')
while True:
    tampilan()