from queue import LifoQueue
stack = LifoQueue()
undo_stack = LifoQueue() 
while True:
    print(45*'=')
    print(f'Riwayat Pencarian Saat Ini: {list(stack.queue)}')
    print('''Pilihan: 
    1. Tambah Pencarian
    2. Hapus Pencarian Terakhir
    3. Undo
    4. Keluar''')
    print(45*'=')
    pilihan = input('Pilih Operasi (1/2/3/4): ')
    if pilihan == '1':
        kata_kunci = input('Masukkan Kata Kunci Pencarian: ')
        stack.put(kata_kunci)
        print(f'{kata_kunci} Ditambahkan Ke Riwayat Pencarian')
    elif pilihan == '2':
        terakhir = stack.get()
        undo_stack.put(terakhir)
        print(f'{terakhir} Dihapus Dari Riwayat Pencarian')
    elif pilihan == '3':
        if not undo_stack.empty():
            terakhir_dihapus = undo_stack.get()
            stack.put(terakhir_dihapus)
            print(f'{terakhir_dihapus} Dikembalikan Ke Riwayat Pencarian')
        else:
            print('Tidak Ada Operasi Yang Bisa Di-undo')
    elif pilihan == '4':
        print('Keluar dari program.')
        exit()
    else:
        print('Pilihan tidak valid.')