class SearchHistory:
    def __init__(self):
        self.history = []  # Stack untuk menyimpan riwayat pencarian
        self.deleted = []  # Stack untuk menyimpan pencarian yang dihapus

    def add_search(self, search_term):
        self.history.append(search_term)
        print(f'Pencarian "{search_term}" telah ditambahkan.')

    def delete_last_search(self):
        if self.history:
            last_search = self.history.pop()
            self.deleted.append(last_search)
            print(f'Pencarian terakhir "{last_search}" telah dihapus.')
        else:
            print('Tidak ada pencarian yang dapat dihapus.')

    def undo_last_delete(self):
        if self.deleted:
            last_deleted = self.deleted.pop()
            self.history.append(last_deleted)
            print(f'Pencarian "{last_deleted}" telah dikembalikan.')
        else:
            print('Tidak ada pencarian yang dapat dikembalikan.')

    def show_history(self):
        if self.history:
            print('Riwayat Pencarian:')
            for i, search in enumerate(self.history, 1):
                print(f'{i}. {search}')
        else:
            print('Riwayat pencarian kosong.')

def main():
    search_history = SearchHistory()
    
    while True:
        print('\nMenu:')
        print('1. Tambah Pencarian')
        print('2. Hapus Pencarian Terakhir')
        print('3. Undo')
        print('4. Tampilkan Riwayat')
        print('5. Keluar')
        
        choice = input('Pilih opsi: ')
        
        if choice == '1':
            search_term = input('Masukkan istilah pencarian: ')
            search_history.add_search(search_term)
        elif choice == '2':
            search_history.delete_last_search()
        elif choice == '3':
            search_history.undo_last_delete()
        elif choice == '4':
            search_history.show_history()
        elif choice == '5':
            print('Keluar dari program.')
            break
        else:
            print('Opsi tidak valid. Silakan coba lagi.')

if __name__ == '__main__':
    main()
